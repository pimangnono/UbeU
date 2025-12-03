import Link from 'next/link';
import styles from './report.module.css';

export default function AssessmentReportPage({ params }: { params: { id: string } }) {
    // Mock data for the report
    const report = {
        id: params.id,
        candidateName: 'Alex Johnson',
        role: 'Senior Audit Manager',
        date: 'Dec 2, 2024',
        overallScore: 85,
        status: 'Recommended',
        softSkills: [
            { name: 'Communication', score: 90, feedback: 'Clear and concise articulation of issues.' },
            { name: 'Empathy', score: 75, feedback: 'Good, but could acknowledge client stress more directly.' },
            { name: 'Leadership', score: 88, feedback: 'Strong command of the situation and proposed confident solutions.' },
        ],
        hardSkills: [
            { name: 'Technical Knowledge', score: 92, feedback: 'Correctly identified the discrepancy and its implications.' },
            { name: 'Compliance', score: 85, feedback: 'Adhered to all regulatory standards in the proposal.' },
        ],
        summary: 'Alex demonstrated strong technical competence and handled the client\'s defensiveness well. The proposed solution was practical and legally sound. Minor improvement needed in validating the client\'s feelings before moving to the solution.',
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <div className={styles.breadcrumbs}>
                    <Link href="/dashboard">Dashboard</Link> / <Link href="/dashboard/candidates">Candidates</Link> / Report
                </div>
                <div className={styles.headerContent}>
                    <div>
                        <h1>Assessment Report</h1>
                        <p className={styles.meta}>{report.candidateName} • {report.role} • {report.date}</p>
                    </div>
                    <div className={styles.statusBadge}>
                        {report.status}
                    </div>
                </div>
            </header>

            <div className={styles.grid}>
                <section className={styles.mainCard}>
                    <div className={styles.scoreSection}>
                        <div className={styles.scoreCircle}>
                            <span className={styles.scoreValue}>{report.overallScore}</span>
                            <span className={styles.scoreLabel}>Overall Score</span>
                        </div>
                        <div className={styles.summary}>
                            <h3>Executive Summary</h3>
                            <p>{report.summary}</p>
                        </div>
                    </div>
                </section>

                <section className={styles.skillsGrid}>
                    <div className={styles.card}>
                        <h3>Soft Skills</h3>
                        <div className={styles.skillList}>
                            {report.softSkills.map((skill) => (
                                <div key={skill.name} className={styles.skillItem}>
                                    <div className={styles.skillHeader}>
                                        <span className={styles.skillName}>{skill.name}</span>
                                        <span className={styles.skillScore}>{skill.score}%</span>
                                    </div>
                                    <div className={styles.progressBar}>
                                        <div className={styles.progressFill} style={{ width: `${skill.score}%` }}></div>
                                    </div>
                                    <p className={styles.skillFeedback}>{skill.feedback}</p>
                                </div>
                            ))}
                        </div>
                    </div>

                    <div className={styles.card}>
                        <h3>Hard Skills</h3>
                        <div className={styles.skillList}>
                            {report.hardSkills.map((skill) => (
                                <div key={skill.name} className={styles.skillItem}>
                                    <div className={styles.skillHeader}>
                                        <span className={styles.skillName}>{skill.name}</span>
                                        <span className={styles.skillScore}>{skill.score}%</span>
                                    </div>
                                    <div className={styles.progressBar}>
                                        <div className={styles.progressFill} style={{ width: `${skill.score}%` }}></div>
                                    </div>
                                    <p className={styles.skillFeedback}>{skill.feedback}</p>
                                </div>
                            ))}
                        </div>
                    </div>
                </section>

                <section className={styles.card}>
                    <h3>AI Interviewer Notes</h3>
                    <div className={styles.notes}>
                        <p>The candidate started the conversation with a professional greeting but seemed slightly nervous when challenged about the error. However, they quickly regained composure and used data to back up their claims without being aggressive. This indicates good resilience and preparation.</p>
                    </div>
                </section>
            </div>
        </div>
    );
}
