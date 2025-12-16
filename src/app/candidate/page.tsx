'use client';

import Link from 'next/link';
import styles from './candidate.module.css';

const mockAssessments = [
    {
        id: '1',
        title: 'Daily Coffee Consumption in Singapore',
        company: 'Acme Corp',
        type: 'Group Case Study',
        duration: '45 min',
        status: 'pending',
        dueDate: '2024-12-20'
    },
    {
        id: '2',
        title: 'E-commerce Platform Strategy',
        company: 'Acme Corp',
        type: '1-to-1 Interview',
        duration: '60 min',
        status: 'completed',
        dueDate: '2024-12-15'
    }
];

export default function CandidateDashboard() {
    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <div className={styles.headerContent}>
                    <h1>UbeU</h1>
                    <Link href="/login" className={styles.logoutBtn}>
                        Sign Out
                    </Link>
                </div>
            </header>

            <main className={styles.main}>
                <div className={styles.welcome}>
                    <h2>Welcome back, Alex!</h2>
                    <p>You have 1 pending assessment</p>
                </div>

                <section className={styles.section}>
                    <h3>Your Assessments</h3>
                    <div className={styles.assessmentList}>
                        {mockAssessments.map((assessment) => (
                            <div key={assessment.id} className={styles.assessmentCard}>
                                <div className={styles.cardContent}>
                                    <h4>{assessment.title}</h4>
                                    <p className={styles.company}>{assessment.company}</p>
                                    <div className={styles.meta}>
                                        <span>{assessment.type}</span>
                                        <span>•</span>
                                        <span>{assessment.duration}</span>
                                    </div>
                                </div>
                                <div className={styles.cardActions}>
                                    <span className={`${styles.status} ${styles[assessment.status]}`}>
                                        {assessment.status === 'pending' ? 'Pending' : 'Completed'}
                                    </span>
                                    {assessment.status === 'pending' ? (
                                        <Link href={`/candidate/assessment/${assessment.id}`} className={styles.startBtn}>
                                            Start Assessment
                                        </Link>
                                    ) : (
                                        <Link href={`/candidate/assessment/${assessment.id}/result`} className={styles.viewBtn}>
                                            View Results
                                        </Link>
                                    )}
                                </div>
                            </div>
                        ))}
                    </div>
                </section>
            </main>
        </div>
    );
}
