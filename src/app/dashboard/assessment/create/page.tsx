'use client';

import { useState } from 'react';
import { sectors, difficultyLevels, timeDurations, interviewTypes, assessmentCategories } from '@/data/mockData';
import Combobox from '@/components/ui/Combobox';
import styles from './create.module.css';

export default function CreateAssessmentPage() {
    const [selectedSector, setSelectedSector] = useState('');
    const [selectedTrack, setSelectedTrack] = useState('');
    const [selectedRole, setSelectedRole] = useState('');
    const [difficulty, setDifficulty] = useState('fresh-grad');

    // New State Variables
    const [duration, setDuration] = useState('45');
    const [customDuration, setCustomDuration] = useState('');
    const [interviewType, setInterviewType] = useState('1-to-1');
    const [selectedCategory, setSelectedCategory] = useState('');
    const [selectedSubcategory, setSelectedSubcategory] = useState('');

    const [isGenerating, setIsGenerating] = useState(false);

    const currentSector = sectors.find((s) => s.id === selectedSector);
    const currentTrack = currentSector?.tracks.find((t) => t.id === selectedTrack);
    const currentCategory = assessmentCategories.find(c => c.id === selectedCategory);

    const handleGenerate = () => {
        setIsGenerating(true);
        // Simulate AI generation delay
        setTimeout(() => {
            setIsGenerating(false);
            // Proceed to next step (mock)
            alert('Proceeding to next step...');
        }, 1500);
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <h1>Create New Assessment</h1>
                <p>Configure the role and assessment details to generate a tailored interview scenario.</p>
            </header>

            <div className={styles.grid}>
                <section className={styles.configSection}>
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
                            onChange={(val) => setSelectedRole(val)}
                            placeholder="Select or type role..."
                            disabled={!selectedTrack}
                        />
                    </div>

                    {/* Step 2: Assessment Details */}
                    <div className={styles.step}>
                        <span className={styles.stepNumber}>2</span>
                        <h3>Assessment Details</h3>
                    </div>

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
                        onClick={handleGenerate}
                        disabled={!selectedRole || !selectedSubcategory || isGenerating}
                    >
                        {isGenerating ? 'Processing...' : 'Next Step'}
                    </button>
                </section>
            </div>
        </div>
    );
}
