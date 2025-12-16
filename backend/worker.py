# worker.py
"""
Celery Worker - Background processing for long-term memory extraction.
Extracts skills and personality traits from interview responses using LLM.
"""

import json
import os
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI

from backend.celery_config import celery_app
from backend.schema_config import (
    GRAPH_INSTRUCTIONS,
    is_valid_skill,
    is_valid_trait,
    get_skill_domain
)

load_dotenv()

# OpenAI client for extraction
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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


def extract_observations(text: str) -> list[dict]:
    """
    Use LLM to extract skills and traits from candidate text.
    Returns a list of structured observations.
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": GRAPH_INSTRUCTIONS},
            {"role": "user", "content": f"Analyze this candidate response:\n\n\"{text}\""}
        ],
        response_format={"type": "json_object"},
        max_tokens=1000
    )
    
    try:
        result = json.loads(response.choices[0].message.content)
        # Handle both single observation and array
        observations = result.get("observations", [result])
        if not isinstance(observations, list):
            observations = [observations]
        return observations
    except (json.JSONDecodeError, KeyError):
        return []


def save_observation_to_graph(
    session_id: str,
    skill: Optional[str],
    skill_domain: Optional[str],
    trait: Optional[str],
    trait_intensity: Optional[str],
    evidence: str
) -> bool:
    """
    Save an extracted observation to Neo4j graph.
    Creates nodes and relationships as per schema.
    """
    driver = get_neo4j_driver()
    
    with driver.session() as session:
        # Ensure Candidate node exists
        session.run("""
            MERGE (c:Candidate {session_id: $session_id})
            ON CREATE SET c.created_at = datetime()
        """, session_id=session_id)
        
        # Create Evidence node
        evidence_query = """
            MATCH (c:Candidate {session_id: $session_id})
            CREATE (e:Evidence {
                text: $evidence,
                timestamp: datetime(),
                id: randomUUID()
            })
            CREATE (c)-[:DEMONSTRATED]->(e)
            RETURN e.id as evidence_id
        """
        result = session.run(evidence_query, session_id=session_id, evidence=evidence)
        evidence_id = result.single()["evidence_id"]
        
        # Link to Skill if present
        if skill and is_valid_skill(skill):
            session.run("""
                MATCH (e:Evidence {id: $evidence_id})
                MERGE (s:Skill {name: $skill})
                ON CREATE SET s.domain = $domain
                CREATE (e)-[:INDICATES]->(s)
            """, evidence_id=evidence_id, skill=skill, domain=skill_domain or get_skill_domain(skill))
        
        # Link to Trait if present
        if trait and is_valid_trait(trait):
            session.run("""
                MATCH (e:Evidence {id: $evidence_id})
                MERGE (t:Trait {name: $trait})
                CREATE (e)-[r:INDICATES {intensity: $intensity}]->(t)
            """, evidence_id=evidence_id, trait=trait, intensity=trait_intensity or "Moderate")
    
    return True


@celery_app.task(bind=True, max_retries=3)
def process_interview_segment(self, session_id: str, user_text: str):
    """
    Celery task to process interview text and extract to knowledge graph.
    
    This runs asynchronously - user doesn't wait for this to complete.
    """
    try:
        # Extract observations using LLM
        observations = extract_observations(user_text)
        
        if not observations:
            return {"status": "no_observations", "session_id": session_id}
        
        saved_count = 0
        for obs in observations:
            skill = obs.get("skill")
            skill_domain = obs.get("skill_domain")
            trait = obs.get("trait")
            trait_intensity = obs.get("trait_intensity")
            evidence = obs.get("evidence", user_text[:200])
            
            # Only save if we found something meaningful
            if skill or trait:
                save_observation_to_graph(
                    session_id=session_id,
                    skill=skill,
                    skill_domain=skill_domain,
                    trait=trait,
                    trait_intensity=trait_intensity,
                    evidence=evidence
                )
                saved_count += 1
        
        return {
            "status": "success",
            "session_id": session_id,
            "observations_saved": saved_count
        }
        
    except Exception as e:
        # Retry on failure
        raise self.retry(exc=e, countdown=5)
