# report_service.py
"""
Report Service - Query structured data from Neo4j knowledge graph.
Generates assessment reports from extracted skills and traits.
"""

import os
from typing import Optional
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

# Neo4j connection (lazy loaded)
_neo4j_driver = None

def get_neo4j_driver():
    """Lazy load Neo4j driver."""
    global _neo4j_driver
    if _neo4j_driver is None:
        from neo4j import GraphDatabase
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "password")
        _neo4j_driver = GraphDatabase.driver(uri, auth=(user, password))
    return _neo4j_driver


def get_skills_with_evidence(session_id: str) -> list[dict]:
    """
    Get all skills demonstrated by the candidate with supporting evidence.
    Groups by skill domain.
    """
    driver = get_neo4j_driver()
    
    query = """
    MATCH (c:Candidate {session_id: $session_id})
    MATCH (c)-[:DEMONSTRATED]->(e:Evidence)-[:INDICATES]->(s:Skill)
    RETURN s.name as skill, s.domain as domain, collect(e.text) as evidence_points
    ORDER BY domain, skill
    """
    
    with driver.session() as session:
        result = session.run(query, session_id=session_id)
        return [record.data() for record in result]


def get_traits_with_evidence(session_id: str) -> list[dict]:
    """
    Get all personality traits exhibited by the candidate with supporting evidence.
    Includes intensity levels.
    """
    driver = get_neo4j_driver()
    
    query = """
    MATCH (c:Candidate {session_id: $session_id})
    MATCH (c)-[:DEMONSTRATED]->(e:Evidence)-[r:INDICATES]->(t:Trait)
    RETURN t.name as trait, 
           collect({text: e.text, intensity: r.intensity}) as evidence_points
    ORDER BY trait
    """
    
    with driver.session() as session:
        result = session.run(query, session_id=session_id)
        return [record.data() for record in result]


def get_candidate_report(session_id: str) -> dict:
    """
    Generate a complete assessment report for a candidate.
    
    Returns structured data with:
    - Skills grouped by CCS domain
    - OCEAN traits with intensity assessments
    - Summary statistics
    """
    skills_data = get_skills_with_evidence(session_id)
    traits_data = get_traits_with_evidence(session_id)
    
    # Group skills by domain
    skills_by_domain = defaultdict(list)
    total_skill_evidence = 0
    
    for item in skills_data:
        domain = item["domain"] or "Uncategorized"
        skills_by_domain[domain].append({
            "skill": item["skill"],
            "evidence_count": len(item["evidence_points"]),
            "evidence_points": item["evidence_points"]
        })
        total_skill_evidence += len(item["evidence_points"])
    
    # Process traits with intensity aggregation
    traits_summary = []
    for item in traits_data:
        evidence_points = item["evidence_points"]
        
        # Determine overall intensity from evidence
        intensities = [ep.get("intensity", "Moderate") for ep in evidence_points]
        if "High" in intensities:
            overall_intensity = "High"
        elif "Low" in intensities:
            overall_intensity = "Low"
        else:
            overall_intensity = "Moderate"
        
        traits_summary.append({
            "trait": item["trait"],
            "intensity": overall_intensity,
            "evidence_count": len(evidence_points),
            "evidence_points": [ep["text"] for ep in evidence_points]
        })
    
    # Generate summary
    strong_domains = [
        domain for domain, skills in skills_by_domain.items() 
        if sum(s["evidence_count"] for s in skills) >= 3
    ]
    
    return {
        "session_id": session_id,
        "summary": {
            "total_skill_evidence": total_skill_evidence,
            "total_trait_evidence": sum(t["evidence_count"] for t in traits_summary),
            "strong_domains": strong_domains,
            "skills_demonstrated": len(skills_data),
            "traits_identified": len(traits_summary)
        },
        "skills_by_domain": dict(skills_by_domain),
        "traits": traits_summary
    }


def get_domain_deep_dive(session_id: str, domain: str) -> dict:
    """
    Get detailed analysis for a specific CCS domain.
    """
    driver = get_neo4j_driver()
    
    query = """
    MATCH (c:Candidate {session_id: $session_id})
    MATCH (c)-[:DEMONSTRATED]->(e:Evidence)-[:INDICATES]->(s:Skill {domain: $domain})
    RETURN s.name as skill, e.text as evidence, e.timestamp as timestamp
    ORDER BY s.name, e.timestamp
    """
    
    with driver.session() as session:
        result = session.run(query, session_id=session_id, domain=domain)
        records = [record.data() for record in result]
    
    # Group by skill
    skills = defaultdict(list)
    for record in records:
        skills[record["skill"]].append({
            "evidence": record["evidence"],
            "timestamp": str(record["timestamp"]) if record["timestamp"] else None
        })
    
    return {
        "domain": domain,
        "skills": dict(skills)
    }
