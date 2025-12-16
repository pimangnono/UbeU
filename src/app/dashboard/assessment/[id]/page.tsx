'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import styles from './assessment.module.css';

// Mock assessment data (same as list page)
const mockAssessments: Record<string, any> = {
    '1': {
        id: '1',
        title: 'Daily Coffee Consumption in Singapore',
        track: 'Data Analytics',
        category: 'Problem-Solving / Analytical',
        subcategory: 'Guesstimation',
        status: 'opened',
        difficulty: 'Fresh Graduate',
        duration: '45 min',
        interviewType: 'AI Group Case Study',
        assigned: ['Alex Johnson', 'Sarah Lee'],
        createdAt: '2024-12-10',
        scenarioContent: `This assessment places candidates in a fast-paced, collaborative environment where they must estimate how many cups of coffee or coffee beverages are consumed in Singapore on a typical day.
The scenario is divided into four structured tasks designed to evaluate analytical thinking, teamwork, communication, and adaptability.

⸻

Task 1 — The Briefing

Scenario Overview:
Candidates receive the business problem and must align as a team on an overall approach for estimating daily national coffee consumption.
Focus is on framing, structuring, and clarity of thought.

⸻

Task 2 — Data Analysis

Scenario Overview:
Candidates review a set of incomplete, mixed-quality data points related to population, consumption behavior, and coffee sales.
They must interpret the information, identify what is relevant, and decide how it will inform their model.

⸻

Task 3 — Quantitative Challenge

Scenario Overview:
Teams convert their framework and selected data into a first numerical estimate.
A mid-task update may introduce an additional requirement, prompting recalibration.

⸻

Task 4 — Synthesis & Recommendation

Scenario Overview:
Candidates consolidate their analysis into a single team estimate and synthesize key assumptions, uncertainties, and implications for the business.`,
        personas: [
            {
                name: 'The Skeptical Colleague',
                role: 'Challenge Bot A',
                purpose: 'Tests the candidate\'s ability to justify assumptions and refine logic under scrutiny.',
                behaviouralCharacteristics: '- Challenges assumptions immediately\n- Emotionally flat, logical\n- Wants clear definitions before moving on\n- Does not accept "gut feel"',
                exampleBehaviours: '"What\'s your evidence for that assumption?"\n"Before calculating, we need a precise definition. What counts as \'coffee\' here?"',
                oceanTrait: 'Openness',
                oceanLevel: 'Low'
            },
            {
                name: 'The Detail-Oriented Analyst',
                role: 'Challenge Bot B',
                purpose: 'Identifies whether the candidate can correct mistakes collaboratively without getting flustered.',
                behaviouralCharacteristics: '- Checks every number\n- Looks for inconsistencies\n- Less about "concepts," more about "math integrity"',
                exampleBehaviours: '"Your estimate implies 8 million cups a day. Singapore only has 5.6 million people—does this add up?"',
                oceanTrait: 'Conscientiousness',
                oceanLevel: 'High'
            },
            {
                name: 'The Overconfident Peer',
                role: 'Challenge Bot C',
                purpose: 'Tests whether the candidate can diplomatically manage an overly dominant team member.',
                behaviouralCharacteristics: '- Pushes quick conclusions\n- Dismisses nuance\n- Interrupts occasionally',
                exampleBehaviours: '"This is easy. Just multiply the population by one cup per day."\n"We\'re wasting time on tiny details."',
                oceanTrait: 'Extraversion',
                oceanLevel: 'High'
            },
            {
                name: 'The Anxious Junior',
                role: 'Support Bot',
                purpose: 'Tests whether candidate provides psychological safety and clear guidance.',
                behaviouralCharacteristics: '- Seeks reassurance often\n- Hesitates to take responsibility\n- Lacks confidence in numbers and ideas',
                exampleBehaviours: '"I\'m afraid I might miscalculate… maybe someone else should do it?"\n"I\'m not sure how to help… what should I do?"',
                oceanTrait: 'Agreeableness',
                oceanLevel: 'High'
            },
            {
                name: 'Rushed Manager',
                role: 'Authority Bot',
                purpose: 'Evaluates whether candidate can stay composed and distill information effectively.',
                behaviouralCharacteristics: '- Demands concise updates\n- Interrupts if answers are too long\n- Focuses only on key assumptions and progress',
                exampleBehaviours: '"I only have one minute. What\'s your current estimate, and what are the top three assumptions?"',
                oceanTrait: 'Conscientiousness',
                oceanLevel: 'High'
            },
            {
                name: 'The Quiet but Insightful Colleague',
                role: 'Inclusivity Tester',
                purpose: 'Assesses whether the candidate actively draws people in.',
                behaviouralCharacteristics: '- Rarely speaks voluntarily\n- Has strong but hidden insights\n- Watches team dynamics closely',
                exampleBehaviours: 'Early: "I\'m okay… you all can continue."\nIf explicitly invited: "One thought—CBD and office districts might inflate per-capita consumption."',
                oceanTrait: 'Extraversion',
                oceanLevel: 'Low'
            }
        ]
    },
    '2': {
        id: '2',
        title: 'E-commerce Platform Strategy',
        track: 'Business Development',
        category: 'Case-Based',
        subcategory: 'Business Case Study',
        status: 'opened',
        difficulty: 'Senior',
        duration: '60 min',
        interviewType: '1-to-1 AI Interview',
        assigned: ['Mike Chen', 'Emma Davis'],
        createdAt: '2024-12-08',
        scenarioContent: `You are a strategy consultant hired by a mid-sized e-commerce company facing slowing growth. The CEO has asked you to evaluate their current position and recommend a path forward.

The company currently sells home goods and has seen 15% YoY growth decline over the past 2 years. Competition from larger marketplaces is intensifying.

Your task is to:
1. Analyze the competitive landscape
2. Identify key growth opportunities
3. Develop a strategic recommendation with clear implementation steps`,
        personas: [
            {
                name: 'CEO',
                role: 'Authority Bot',
                purpose: 'Tests executive communication and strategic thinking.',
                oceanTrait: 'Conscientiousness',
                oceanLevel: 'High'
            }
        ]
    }
};

// Default assessment for unknown IDs
const defaultAssessment = {
    id: '0',
    title: 'Assessment Not Found',
    track: 'Unknown',
    category: 'Unknown',
    subcategory: 'Unknown',
    status: 'inactive',
    difficulty: 'Unknown',
    duration: 'N/A',
    interviewType: 'N/A',
    assigned: [],
    createdAt: 'N/A',
    scenarioContent: 'This assessment does not exist or has been deleted.',
    personas: []
};

export default function AssessmentDetailPage() {
    const params = useParams();
    const id = params.id as string;
    const assessment = mockAssessments[id] || defaultAssessment;
    const [isEditing, setIsEditing] = useState(false);

    const getStatusClass = (status: string) => {
        switch (status) {
            case 'opened': return styles.statusOpened;
            case 'inactive': return styles.statusInactive;
            case 'closed': return styles.statusClosed;
            default: return '';
        }
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <div className={styles.breadcrumbs}>
                    <Link href="/dashboard">Dashboard</Link> / <Link href="/dashboard/assessments">Assessments</Link> / {assessment.title}
                </div>
                <div className={styles.headerContent}>
                    <div className={styles.headerLeft}>
                        <h1>{assessment.title}</h1>
                        <div className={styles.metaRow}>
                            <span className={styles.trackBadge}>{assessment.track}</span>
                            <span className={`${styles.statusBadge} ${getStatusClass(assessment.status)}`}>
                                {assessment.status}
                            </span>
                            <span className={styles.meta}>
                                {assessment.difficulty} • {assessment.duration} • {assessment.interviewType}
                            </span>
                        </div>
                    </div>
                    <div className={styles.headerActions}>
                        <button
                            className={`${styles.btn} ${isEditing ? styles.btnPrimary : styles.btnOutline}`}
                            onClick={() => setIsEditing(!isEditing)}
                        >
                            {isEditing ? 'Save Changes' : 'Edit Assessment'}
                        </button>
                    </div>
                </div>
            </header>

            <div className={styles.grid}>
                {/* Assessment Details Card */}
                <section className={styles.card}>
                    <div className={styles.cardHeader}>
                        <h3>Assessment Details</h3>
                    </div>
                    <div className={styles.detailsGrid}>
                        <div className={styles.detailItem}>
                            <span className={styles.detailLabel}>Category</span>
                            <span className={styles.detailValue}>{assessment.category}</span>
                        </div>
                        <div className={styles.detailItem}>
                            <span className={styles.detailLabel}>Subcategory</span>
                            <span className={styles.detailValue}>{assessment.subcategory}</span>
                        </div>
                        <div className={styles.detailItem}>
                            <span className={styles.detailLabel}>Created</span>
                            <span className={styles.detailValue}>{assessment.createdAt}</span>
                        </div>
                        <div className={styles.detailItem}>
                            <span className={styles.detailLabel}>Assigned Candidates</span>
                            <div className={styles.assignedList}>
                                {assessment.assigned.length > 0 ? (
                                    assessment.assigned.map((name: string, i: number) => (
                                        <span key={i} className={styles.assignedBadge}>{name}</span>
                                    ))
                                ) : (
                                    <span className={styles.noAssigned}>No candidates assigned</span>
                                )}
                            </div>
                        </div>
                    </div>
                </section>

                {/* Scenario Content Card */}
                <section className={styles.card}>
                    <div className={styles.cardHeader}>
                        <h3>Scenario Content</h3>
                    </div>
                    {isEditing ? (
                        <textarea
                            className={styles.scenarioTextarea}
                            defaultValue={assessment.scenarioContent}
                            rows={15}
                        />
                    ) : (
                        <div className={styles.scenarioContent}>
                            {assessment.scenarioContent.split('\n').map((line: string, i: number) => (
                                <p key={i}>{line || <br />}</p>
                            ))}
                        </div>
                    )}
                </section>

                {/* AI Personas Card */}
                <section className={styles.card}>
                    <div className={styles.cardHeader}>
                        <h3>AI Personas ({assessment.personas.length})</h3>
                    </div>
                    <div className={styles.personaGrid}>
                        {assessment.personas.map((persona: any, i: number) => (
                            <div key={i} className={`${styles.personaCard} ${isEditing ? styles.personaCardEditing : ''}`}>
                                {isEditing ? (
                                    <>
                                        <div className={styles.editField}>
                                            <label>Name</label>
                                            <input type="text" defaultValue={persona.name} className={styles.editInput} />
                                        </div>
                                        <div className={styles.editField}>
                                            <label>Role</label>
                                            <input type="text" defaultValue={persona.role} className={styles.editInput} />
                                        </div>
                                        <div className={styles.editField}>
                                            <label>Purpose</label>
                                            <textarea defaultValue={persona.purpose} className={styles.editTextarea} rows={2} />
                                        </div>
                                        <div className={styles.editField}>
                                            <label>Behavioural Characteristics</label>
                                            <textarea defaultValue={persona.behaviouralCharacteristics} className={styles.editTextarea} rows={3} />
                                        </div>
                                        <div className={styles.editField}>
                                            <label>Example Behaviours</label>
                                            <textarea defaultValue={persona.exampleBehaviours} className={styles.editTextarea} rows={2} />
                                        </div>
                                        <div className={styles.editFieldRow}>
                                            <div className={styles.editField}>
                                                <label>OCEAN Trait</label>
                                                <select defaultValue={persona.oceanTrait} className={styles.editSelect}>
                                                    <option value="Openness">Openness</option>
                                                    <option value="Conscientiousness">Conscientiousness</option>
                                                    <option value="Extraversion">Extraversion</option>
                                                    <option value="Agreeableness">Agreeableness</option>
                                                    <option value="Neuroticism">Neuroticism</option>
                                                </select>
                                            </div>
                                            <div className={styles.editField}>
                                                <label>Level</label>
                                                <select defaultValue={persona.oceanLevel} className={styles.editSelect}>
                                                    <option value="Low">Low</option>
                                                    <option value="Medium">Medium</option>
                                                    <option value="High">High</option>
                                                </select>
                                            </div>
                                        </div>
                                    </>
                                ) : (
                                    <>
                                        <div className={styles.personaHeader}>
                                            <div className={styles.personaIcon}>
                                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                                </svg>
                                            </div>
                                            <div>
                                                <h4>{persona.name}</h4>
                                                <span className={styles.personaRole}>{persona.role}</span>
                                            </div>
                                        </div>
                                        <p className={styles.personaPurpose}><strong>Purpose:</strong> {persona.purpose}</p>
                                        {persona.behaviouralCharacteristics && (
                                            <div className={styles.personaSection}>
                                                <span className={styles.sectionLabel}>Behaviour:</span>
                                                <p>{persona.behaviouralCharacteristics}</p>
                                            </div>
                                        )}
                                        {persona.exampleBehaviours && (
                                            <div className={styles.personaSection}>
                                                <span className={styles.sectionLabel}>Example:</span>
                                                <p className={styles.exampleText}>{persona.exampleBehaviours}</p>
                                            </div>
                                        )}
                                        <div className={styles.personaTraits}>
                                            <span className={styles.traitBadge}>
                                                {persona.oceanTrait}: {persona.oceanLevel}
                                            </span>
                                        </div>
                                    </>
                                )}
                            </div>
                        ))}
                    </div>
                </section>
            </div>
        </div>
    );
}
