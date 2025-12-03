'use client';

import { useState, useEffect } from 'react';
import { sectors, difficultyLevels, timeDurations, interviewTypes, assessmentCategories, personas } from '@/data/mockData';
import Combobox from '@/components/ui/Combobox';
import styles from './create.module.css';

interface CustomizablePersona {
    id: string;
    name: string;
    role: string;
    behaviouralCharacteristics: string;
    testsFor: string[];
    oceanTrait: string;
    oceanLevel: 'High' | 'Medium' | 'Low';
    purpose: string;
    exampleBehaviours: string;
}

const OCEAN_TRAITS = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'];
const OCEAN_LEVELS = ['High', 'Medium', 'Low'] as const;

const CRITICAL_CORE_SKILLS = [
    {
        category: 'Thinking Critically',
        skills: ['Creative Thinking', 'Decision Making', 'Problem Solving', 'Sense Making', 'Transdisciplinary Thinking']
    },
    {
        category: 'Interacting with Others',
        skills: ['Building Inclusivity', 'Collaboration', 'Communication', 'Customer Orientation', 'Developing People', 'Influence']
    },
    {
        category: 'Staying Relevant',
        skills: ['Adaptability', 'Digital Fluency', 'Global Perspective', 'Learning Agility', 'Self Management']
    }
];

const PREDEFINED_PERSONAS = [
    {
        name: 'The Skeptical Colleague',
        role: 'Challenge Bot A',
        behaviouralCharacteristics: '- Challenges assumptions immediately\n- Emotionally flat, logical\n- Wants clear definitions before moving on\n- Does not accept "gut feel"',
        testsFor: ['Problem Solving', 'Decision Making', 'Influence', 'Communication'],
        oceanTrait: 'Openness',
        oceanLevel: 'Low',
        purpose: 'Tests the candidate’s ability to justify assumptions and refine logic under scrutiny.',
        exampleBehaviours: '“What’s your evidence for that assumption?”\n“Before calculating, we need a precise definition. What counts as ‘coffee’ here?”'
    },
    {
        name: 'The Detail-Oriented Analyst',
        role: 'Challenge Bot B',
        behaviouralCharacteristics: '- Checks every number\n- Looks for inconsistencies\n- Less about "concepts," more about "math integrity"',
        testsFor: ['Decision Making', 'Digital Fluency', 'Problem Solving'],
        oceanTrait: 'Conscientiousness',
        oceanLevel: 'High',
        purpose: 'Identifies whether the candidate can correct mistakes collaboratively without getting flustered.',
        exampleBehaviours: '“Your estimate implies 8 million cups a day. Singapore only has 5.6 million people—does this add up?”'
    },
    {
        name: 'The Overconfident Peer',
        role: 'Challenge Bot C',
        behaviouralCharacteristics: '- Pushes quick conclusions\n- Dismisses nuance\n- Interrupts occasionally',
        testsFor: ['Collaboration', 'Influence', 'Building Inclusivity'],
        oceanTrait: 'Extraversion',
        oceanLevel: 'High',
        purpose: 'Tests whether the candidate can diplomatically manage an overly dominant team member.',
        exampleBehaviours: '“This is easy. Just multiply the population by one cup per day.”\n“We’re wasting time on tiny details.”'
    },
    {
        name: 'The Anxious Junior',
        role: 'Support Bot',
        behaviouralCharacteristics: '- Seeks reassurance often\n- Hesitates to take responsibility\n- Lacks confidence in numbers and ideas',
        testsFor: ['Developing People', 'Collaboration', 'Communication'],
        oceanTrait: 'Agreeableness',
        oceanLevel: 'High',
        purpose: 'Tests whether candidate provides psychological safety and clear guidance.',
        exampleBehaviours: '“I’m afraid I might miscalculate… maybe someone else should do it?”\n“I’m not sure how to help… what should I do?”'
    },
    {
        name: 'Rushed Manager',
        role: 'Authority Bot',
        behaviouralCharacteristics: '- Demands concise updates\n- Interrupts if answers are too long\n- Focuses only on key assumptions and progress',
        testsFor: ['Communication', 'Decision Making', 'Adaptability'],
        oceanTrait: 'Conscientiousness',
        oceanLevel: 'High',
        purpose: 'Evaluates whether candidate can stay composed and distill information effectively.',
        exampleBehaviours: '“I only have one minute. What’s your current estimate, and what are the top three assumptions?”'
    },
    {
        name: 'The Quiet but Insightful Colleague',
        role: 'Inclusivity Tester',
        behaviouralCharacteristics: '- Rarely speaks voluntarily\n- Has strong but hidden insights\n- Watches team dynamics closely',
        testsFor: ['Building Inclusivity', 'Collaboration'],
        oceanTrait: 'Extraversion',
        oceanLevel: 'Low',
        purpose: 'Assesses whether the candidate actively draws people in.',
        exampleBehaviours: 'Early: “I’m okay… you all can continue.”\nIf explicitly invited: “One thought—CBD and office districts might inflate per-capita consumption.”'
    }
];

const DEFAULT_SCENARIO_TITLE = "Estimation Case: Daily Coffee Consumption in Singapore";
const DEFAULT_SCENARIO_CONTENT = `This assessment places candidates in a fast-paced, collaborative environment where they must estimate how many cups of coffee or coffee beverages are consumed in Singapore on a typical day.
The scenario is divided into four structured tasks designed to evaluate analytical thinking, teamwork, communication, and adaptability.

⸻

Task 1 — The Briefing

Scenario Overview:
Candidates receive the business problem and must align as a team on an overall approach for estimating daily national coffee consumption.
Focus is on framing, structuring, and clarity of thought.

Stimulus:
A short prompt introducing the estimation challenge and asking the team to outline a high-level approach (e.g., population-based model, consumption occasions, or venue segmentation).

⸻

Task 2 — Data Analysis

Scenario Overview:
Candidates review a set of incomplete, mixed-quality data points related to population, consumption behavior, and coffee sales.
They must interpret the information, identify what is relevant, and decide how it will inform their model.

Stimulus:
A curated dataset that includes population numbers, consumption rates, hawker centre volumes, and behavioral benchmarks.

⸻

Task 3 — Quantitative Challenge

Scenario Overview:
Teams convert their framework and selected data into a first numerical estimate.
A mid-task update may introduce an additional requirement, prompting recalibration.

Stimulus:
A request to generate the initial estimate, with a twist such as including canned coffee or home consumption.

⸻

Task 4 — Synthesis & Recommendation

Scenario Overview:
Candidates consolidate their analysis into a single team estimate and synthesize key assumptions, uncertainties, and implications for the business.

Stimulus:
A request for a concise summary of the final estimate, top assumptions, limitations, and a recommended next step for validation.`;

export default function CreateAssessmentPage() {
    const [currentStep, setCurrentStep] = useState(1);
    const [selectedSector, setSelectedSector] = useState('');
    const [selectedTrack, setSelectedTrack] = useState('');
    const [selectedRole, setSelectedRole] = useState('');
    const [difficulty, setDifficulty] = useState('fresh-grad');
    const [selectedSkills, setSelectedSkills] = useState<string[]>([]);

    // New State Variables
    const [duration, setDuration] = useState('45');
    const [customDuration, setCustomDuration] = useState('');
    const [interviewType, setInterviewType] = useState('1-to-1');
    const [selectedCategory, setSelectedCategory] = useState('');
    const [selectedSubcategory, setSelectedSubcategory] = useState('');

    // Advanced Persona State
    const [customPersonas, setCustomPersonas] = useState<CustomizablePersona[]>([]);

    // Scenario State
    const [scenarioTitle, setScenarioTitle] = useState('');
    const [scenarioContent, setScenarioContent] = useState('');

    const [isGenerating, setIsGenerating] = useState(false);

    const currentSector = sectors.find((s) => s.id === selectedSector);
    const currentTrack = currentSector?.tracks.find((t) => t.id === selectedTrack);
    const currentRoleData = currentTrack?.roles.find((r) => r.id === selectedRole);
    const currentCategory = assessmentCategories.find(c => c.id === selectedCategory);
    const currentSubcategory = currentCategory?.templates.find(t => t.id === selectedSubcategory);

    // Initialize Personas and Scenario when entering Step 2
    useEffect(() => {
        if (currentStep === 2) {
            // Initialize Personas
            if (customPersonas.length === 0) {
                // For Mockup: Load ALL predefined personas so the user can see them all
                const initialPersonasData = PREDEFINED_PERSONAS;

                const initialPersonas: CustomizablePersona[] = initialPersonasData.map(p => ({
                    id: crypto.randomUUID(),
                    name: p.name,
                    role: p.role,
                    behaviouralCharacteristics: p.behaviouralCharacteristics,
                    testsFor: p.testsFor,
                    oceanTrait: p.oceanTrait,
                    oceanLevel: p.oceanLevel as any,
                    purpose: p.purpose,
                    exampleBehaviours: p.exampleBehaviours
                }));
                setCustomPersonas(initialPersonas);
            }

            // Initialize Scenario
            if (!scenarioTitle) {
                setScenarioTitle(DEFAULT_SCENARIO_TITLE);
                setScenarioContent(DEFAULT_SCENARIO_CONTENT);
            }
        }
    }, [currentStep, interviewType, customPersonas.length, scenarioTitle]);

    const handleNextStep = () => {
        setIsGenerating(true);
        // Simulate processing delay
        setTimeout(() => {
            setIsGenerating(false);
            setCurrentStep(2);
        }, 1000);
    };

    const handleBack = () => {
        setCurrentStep(1);
    };

    const handleFinalize = () => {
        console.log('Final Personas:', customPersonas);
        console.log('Scenario:', { title: scenarioTitle, content: scenarioContent });
        alert('Assessment Saved! (Check console for data)');
    };

    const toggleSkill = (skillId: string) => {
        setSelectedSkills(prev =>
            prev.includes(skillId)
                ? prev.filter(id => id !== skillId)
                : [...prev, skillId]
        );
    };

    const toggleSelectAll = () => {
        if (!currentRoleData?.skills) return;

        if (selectedSkills.length === currentRoleData.skills.length) {
            setSelectedSkills([]);
        } else {
            setSelectedSkills(currentRoleData.skills.map(s => s.id));
        }
    };

    // Persona Management Functions
    const addPersona = () => {
        setCustomPersonas(prev => [...prev, {
            id: crypto.randomUUID(),
            name: `Interviewer ${prev.length + 1}`,
            role: 'Interviewer',
            behaviouralCharacteristics: '',
            testsFor: [],
            oceanTrait: 'Openness',
            oceanLevel: 'Medium',
            purpose: '',
            exampleBehaviours: ''
        }]);
    };

    const removePersona = (id: string) => {
        if (customPersonas.length <= 1) {
            alert("You must have at least one AI persona.");
            return;
        }
        setCustomPersonas(prev => prev.filter(p => p.id !== id));
    };

    const updatePersona = (id: string, field: keyof CustomizablePersona, value: any) => {
        setCustomPersonas(prev => prev.map(p =>
            p.id === id ? { ...p, [field]: value } : p
        ));
    };

    const togglePersonaSkill = (personaId: string, skillName: string) => {
        setCustomPersonas(prev => prev.map(p => {
            if (p.id !== personaId) return p;
            const newTestsFor = p.testsFor.includes(skillName)
                ? p.testsFor.filter(s => s !== skillName)
                : [...p.testsFor, skillName];
            return { ...p, testsFor: newTestsFor };
        }));
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1>Create New Assessment</h1>
                <p>Configure the role and assessment details to generate a tailored interview scenario.</p>
            </header>

            <div className={styles.grid}>
                <section className={styles.configSection}>
                    {currentStep === 1 ? (
                        <>
                            {/* Step 1: Role Selection */}
                            <div className={styles.step}>
                                <span className={styles.stepNumber}>1</span>
                                <h3>Role Selection</h3>
                            </div>

                            <div className={styles.formGroup}>
                                <Combobox
                                    label="Sector"
                                    options={sectors}
                                    value={selectedSector}
                                    onChange={(val) => {
                                        setSelectedSector(val);
                                        setSelectedTrack('');
                                        setSelectedRole('');
                                        setSelectedSkills([]);
                                    }}
                                    placeholder="Select or type sector..."
                                />
                            </div>

                            <div className={styles.formGroup}>
                                <Combobox
                                    label="Track"
                                    options={currentSector?.tracks || []}
                                    value={selectedTrack}
                                    onChange={(val) => {
                                        setSelectedTrack(val);
                                        setSelectedRole('');
                                        setSelectedSkills([]);
                                    }}
                                    placeholder="Select or type track..."
                                    disabled={!selectedSector}
                                />
                            </div>

                            <div className={styles.formGroup}>
                                <Combobox
                                    label="Job Role"
                                    options={currentTrack?.roles || []}
                                    value={selectedRole}
                                    onChange={(val) => {
                                        setSelectedRole(val);
                                        setSelectedSkills([]);
                                    }}
                                    placeholder="Select or type role..."
                                    disabled={!selectedTrack}
                                />
                            </div>

                            {/* Step 2: Assessment Details */}
                            <div className={styles.step}>
                                <span className={styles.stepNumber}>2</span>
                                <h3>Assessment Details</h3>
                            </div>

                            {currentRoleData?.skills && currentRoleData.skills.length > 0 && (
                                <div className={styles.formGroup}>
                                    <div className={styles.labelRow}>
                                        <label>Critical Core Skills</label>
                                        <button
                                            onClick={toggleSelectAll}
                                            className={styles.selectAllBtn}
                                            type="button"
                                        >
                                            {selectedSkills.length === currentRoleData.skills.length ? 'Deselect All' : 'Select All'}
                                        </button>
                                    </div>
                                    <div className={styles.optionsGrid}>
                                        {currentRoleData.skills.map((skill) => (
                                            <div key={skill.id} className={styles.tooltipWrapper}>
                                                <button
                                                    className={`${styles.optionCard} ${selectedSkills.includes(skill.id) ? styles.selected : ''}`}
                                                    onClick={() => toggleSkill(skill.id)}
                                                >
                                                    <span className={styles.optionLabel}>{skill.label}</span>
                                                    <span className={styles.optionDesc}>Level {skill.proficiencyLevel}</span>
                                                </button>
                                                <div className={styles.tooltip}>
                                                    <strong>{skill.label}</strong>
                                                    <p>{skill.description}</p>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            <div className={styles.formGroup}>
                                <label>Difficulty Level</label>
                                <div className={styles.optionsGrid}>
                                    {difficultyLevels.map((level) => (
                                        <button
                                            key={level.id}
                                            className={`${styles.optionCard} ${difficulty === level.id ? styles.selected : ''}`}
                                            onClick={() => setDifficulty(level.id)}
                                        >
                                            <span className={styles.optionLabel}>{level.label}</span>
                                            <span className={styles.optionDesc}>{level.description}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            <div className={styles.formGroup}>
                                <label>Duration</label>
                                <div className={styles.durationContainer}>
                                    {timeDurations.map((d) => (
                                        <button
                                            key={d.id}
                                            className={`${styles.pillBtn} ${duration === d.id ? styles.selected : ''}`}
                                            onClick={() => {
                                                setDuration(d.id);
                                                setCustomDuration('');
                                            }}
                                        >
                                            {d.label}
                                        </button>
                                    ))}
                                    <input
                                        type="text"
                                        placeholder="Custom (min)"
                                        className={`${styles.customInput} ${!timeDurations.find(d => d.id === duration) ? styles.selectedInput : ''}`}
                                        value={customDuration}
                                        onChange={(e) => {
                                            setCustomDuration(e.target.value);
                                            setDuration('custom');
                                        }}
                                        onClick={() => setDuration('custom')}
                                    />
                                </div>
                            </div>

                            <div className={styles.formGroup}>
                                <label>Interview Type</label>
                                <div className={styles.optionsGrid}>
                                    {interviewTypes.map((type) => (
                                        <button
                                            key={type.id}
                                            className={`${styles.optionCard} ${interviewType === type.id ? styles.selected : ''}`}
                                            onClick={() => setInterviewType(type.id)}
                                        >
                                            <span className={styles.optionLabel}>{type.label}</span>
                                            <span className={styles.optionDesc}>{type.description}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* Step 3: Template Selection */}
                            <div className={styles.step}>
                                <span className={styles.stepNumber}>3</span>
                                <h3>Template Selection</h3>
                            </div>

                            <div className={styles.formGroup}>
                                <Combobox
                                    label="Category"
                                    options={assessmentCategories}
                                    value={selectedCategory}
                                    onChange={(val) => {
                                        setSelectedCategory(val);
                                        setSelectedSubcategory('');
                                    }}
                                    placeholder="Select or type category..."
                                />
                            </div>

                            {selectedCategory && (
                                <div className={styles.formGroup}>
                                    <label>Subcategory</label>
                                    <div className={styles.optionsGrid}>
                                        {currentCategory?.templates.map((temp) => (
                                            <div key={temp.id} className={styles.tooltipWrapper}>
                                                <button
                                                    className={`${styles.optionCard} ${selectedSubcategory === temp.id ? styles.selected : ''}`}
                                                    onClick={() => setSelectedSubcategory(temp.id)}
                                                >
                                                    <span className={styles.optionLabel}>{temp.label}</span>
                                                </button>
                                                <div className={styles.tooltip}>
                                                    <strong>{temp.label}</strong>
                                                    <p>{temp.description}</p>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            <button
                                className={`${styles.generateBtn} ${isGenerating ? styles.loading : ''}`}
                                onClick={handleNextStep}
                                disabled={!selectedRole || !selectedSubcategory || isGenerating}
                            >
                                {isGenerating ? 'Processing...' : 'Generate'}
                            </button>
                        </>
                    ) : (
                        <>
                            {/* Step 2 View: Preview & Persona */}
                            <div className={styles.step}>
                                <span className={styles.stepNumber}>4</span>
                                <h3>Review</h3>
                            </div>

                            <div className={styles.mockWarning}>
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                    <circle cx="12" cy="12" r="10"></circle>
                                    <line x1="12" y1="8" x2="12" y2="12"></line>
                                    <line x1="12" y1="16" x2="12.01" y2="16"></line>
                                </svg>
                                <span>This is currently a mock-up page with pre-filled data.</span>
                            </div>

                            <div className={styles.previewBox}>
                                <h4>Assessment Preview</h4>
                                <div className={styles.previewContent}>
                                    <div className={styles.previewField}>
                                        <label>Scenario Title</label>
                                        <input
                                            type="text"
                                            value={scenarioTitle}
                                            onChange={(e) => setScenarioTitle(e.target.value)}
                                            className={styles.scenarioTitleInput}
                                        />
                                    </div>
                                    <div className={styles.previewField}>
                                        <label>Scenario Details</label>
                                        <textarea
                                            value={scenarioContent}
                                            onChange={(e) => setScenarioContent(e.target.value)}
                                            className={styles.scenarioContentInput}
                                            rows={15}
                                        />
                                    </div>
                                    <p className={styles.previewNote}>(You can edit the scenario details above)</p>
                                </div>
                            </div>

                            <div className={styles.formGroup}>
                                <div className={styles.labelRow}>
                                    <label>AI Personas</label>
                                    <button onClick={addPersona} className={styles.addPersonaBtn}>+ Add New Bot</button>
                                </div>
                                <div className={styles.personaList}>
                                    {customPersonas.map((persona, index) => (
                                        <div key={persona.id} className={styles.personaEditorCard}>
                                            <div className={styles.personaHeader}>
                                                <div className={styles.personaTitle}>
                                                    <div className={styles.personaIcon}>
                                                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                                            <path strokeLinecap="round" strokeLinejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                                        </svg>
                                                    </div>
                                                    <input
                                                        type="text"
                                                        value={persona.name}
                                                        onChange={(e) => updatePersona(persona.id, 'name', e.target.value)}
                                                        className={styles.personaNameInput}
                                                        placeholder="Persona Name"
                                                    />
                                                </div>
                                                <button onClick={() => removePersona(persona.id)} className={styles.removeBtn} title="Remove Persona">
                                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="18" height="18">
                                                        <path strokeLinecap="round" strokeLinejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                                    </svg>
                                                </button>
                                            </div>

                                            <div className={styles.editorGrid}>
                                                <div className={styles.fieldGroup}>
                                                    <label>Behavioural Characteristics</label>
                                                    <textarea
                                                        value={persona.behaviouralCharacteristics}
                                                        onChange={(e) => updatePersona(persona.id, 'behaviouralCharacteristics', e.target.value)}
                                                        placeholder="e.g. Professional, strict, friendly..."
                                                        rows={2}
                                                    />
                                                </div>

                                                <div className={styles.fieldGroup}>
                                                    <label>Purpose in Scenario</label>
                                                    <textarea
                                                        value={persona.purpose}
                                                        onChange={(e) => updatePersona(persona.id, 'purpose', e.target.value)}
                                                        placeholder="e.g. To assess technical depth..."
                                                        rows={2}
                                                    />
                                                </div>

                                                <div className={styles.fieldGroup}>
                                                    <label>Example Behaviours</label>
                                                    <textarea
                                                        value={persona.exampleBehaviours}
                                                        onChange={(e) => updatePersona(persona.id, 'exampleBehaviours', e.target.value)}
                                                        placeholder="e.g. Asks clarifying questions..."
                                                        rows={2}
                                                    />
                                                </div>

                                                <div className={styles.fieldGroup}>
                                                    <label>Relevant OCEAN Trait</label>
                                                    <div className={styles.oceanInputs}>
                                                        <select
                                                            value={persona.oceanTrait}
                                                            onChange={(e) => updatePersona(persona.id, 'oceanTrait', e.target.value)}
                                                        >
                                                            {OCEAN_TRAITS.map(t => <option key={t} value={t}>{t}</option>)}
                                                        </select>
                                                        <select
                                                            value={persona.oceanLevel}
                                                            onChange={(e) => updatePersona(persona.id, 'oceanLevel', e.target.value)}
                                                        >
                                                            {OCEAN_LEVELS.map(l => <option key={l} value={l}>{l}</option>)}
                                                        </select>
                                                    </div>
                                                </div>

                                                <div className={`${styles.fieldGroup} ${styles.fullWidth}`}>
                                                    <label>Tests For (Critical Core Skills)</label>
                                                    <div className={styles.skillCategories}>
                                                        {CRITICAL_CORE_SKILLS.map(category => (
                                                            <div key={category.category} className={styles.skillCategory}>
                                                                <span className={styles.categoryLabel}>{category.category}</span>
                                                                <div className={styles.skillTags}>
                                                                    {category.skills.map(skillName => {
                                                                        const isSelected = persona.testsFor.includes(skillName);
                                                                        return (
                                                                            <button
                                                                                key={skillName}
                                                                                className={`${styles.skillTag} ${isSelected ? styles.selected : ''}`}
                                                                                onClick={() => togglePersonaSkill(persona.id, skillName)}
                                                                            >
                                                                                {skillName}
                                                                            </button>
                                                                        );
                                                                    })}
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            <div className={styles.actionButtons}>
                                <button className={styles.backBtn} onClick={handleBack}>
                                    Back
                                </button>
                                <button className={styles.generateBtn} onClick={handleFinalize}>
                                    Save
                                </button>
                            </div>
                        </>
                    )}
                </section>
            </div>
        </div>
    );
}
