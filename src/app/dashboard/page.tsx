import Link from 'next/link';
import styles from './dashboard.module.css';

export default function DashboardPage() {
    return (
        <div className={styles.dashboard}>
            <section className={styles.welcome}>
                <h2>Welcome back, Hiring Manager! 👋</h2>
                <p>Here's what's happening with your assessments today.</p>
            </section>

            <section className={styles.statsGrid}>
                <div className={styles.statCard}>
                    <h3>Active Assessments</h3>
                    <p className={styles.statValue}>12</p>
                    <span className={styles.statTrend}>+2 this week</span>
                </div>
                <div className={styles.statCard}>
                    <h3>Completed Interviews</h3>
                    <p className={styles.statValue}>45</p>
                    <span className={styles.statTrend}>85% completion rate</span>
                </div>
                <div className={styles.statCard}>
                    <h3>Pending Review</h3>
                    <p className={styles.statValue}>8</p>
                    <span className={`${styles.statTrend} ${styles.warning}`}>Action needed</span>
                </div>
            </section>

            <div className={styles.contentGrid}>
                <section className={`${styles.card} ${styles.schedule}`}>
                    <div className={styles.cardHeader}>
                        <h3>Upcoming Schedule</h3>
                        <button className="btn btn-outline">View Calendar</button>
                    </div>
                    <ul className={styles.scheduleList}>
                        <li className={styles.scheduleItem}>
                            <div className={styles.time}>09:00 AM</div>
                            <div className={styles.details}>
                                <h4>Senior Audit Manager</h4>
                                <p>Candidate: Alex Johnson</p>
                            </div>
                            <span className={styles.tag}>Technical</span>
                        </li>
                        <li className={styles.scheduleItem}>
                            <div className={styles.time}>11:30 AM</div>
                            <div className={styles.details}>
                                <h4>Forensic Accountant</h4>
                                <p>Candidate: Sarah Lee</p>
                            </div>
                            <span className={styles.tag}>Behavioral</span>
                        </li>
                        <li className={styles.scheduleItem}>
                            <div className={styles.time}>02:00 PM</div>
                            <div className={styles.details}>
                                <h4>Tax Consultant Intern</h4>
                                <p>Candidate: Mike Chen</p>
                            </div>
                            <span className={styles.tag}>Case Study</span>
                        </li>
                    </ul>
                </section>

                <section className={`${styles.card} ${styles.actions}`}>
                    <div className={styles.cardHeader}>
                        <h3>Quick Actions</h3>
                    </div>
                    <div className={styles.actionButtons}>
                        <Link href="/dashboard/assessment/create" className={`${styles.actionBtn} ${styles.primary}`}>
                            <span className={styles.actionIcon}>✨</span>
                            <div className={styles.actionText}>
                                <h4>Create New Assessment</h4>
                                <p>Design a new AI-driven interview scenario</p>
                            </div>
                        </Link>
                        <button className={styles.actionBtn}>
                            <span className={styles.actionIcon}>👥</span>
                            <div className={styles.actionText}>
                                <h4>Invite Candidates</h4>
                                <p>Send assessment links to applicants</p>
                            </div>
                        </button>
                    </div>
                </section>
            </div>
        </div>
    );
}
