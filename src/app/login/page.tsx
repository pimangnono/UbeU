'use client';

import Link from 'next/link';
import styles from './login.module.css';

const roles = [
    {
        id: 'hr',
        title: 'Hiring Manager',
        description: 'Create and manage assessments, review candidate reports',
        href: '/dashboard'
    },
    {
        id: 'candidate',
        title: 'Candidate',
        description: 'Take assessments and participate in AI interviews',
        href: '/candidate'
    }
];

export default function LoginPage() {
    return (
        <div className={styles.container}>
            <div className={styles.loginCard}>
                <div className={styles.logo}>
                    <h1>UbeU</h1>
                    <p>AI-Powered Interview Platform</p>
                </div>

                <div className={styles.roleSection}>
                    <h2>Select Your Role</h2>
                    <p>Choose how you want to access the platform</p>

                    <div className={styles.roleGrid}>
                        {roles.map((role) => (
                            <Link
                                key={role.id}
                                href={role.href}
                                className={styles.roleCard}
                            >
                                <h3>{role.title}</h3>
                                <p>{role.description}</p>
                            </Link>
                        ))}
                    </div>
                </div>

                <div className={styles.footer}>
                    <p>© 2024 UbeU. All rights reserved.</p>
                </div>
            </div>
        </div>
    );
}
