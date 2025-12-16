'use client';

import Link from 'next/link';
import styles from './Sidebar.module.css';
import { useSidebar } from './SidebarContext';

const navItems = [
    { label: 'Dashboard', href: '/dashboard' },
    { label: 'Assessments', href: '/dashboard/assessments' },
    { label: 'Candidates', href: '/dashboard/candidates' },
    { label: 'Settings', href: '/dashboard/settings' },
];

export default function Sidebar() {
    const { isCollapsed, setIsCollapsed } = useSidebar();

    return (
        <aside className={`${styles.sidebar} ${isCollapsed ? styles.collapsed : ''}`}>
            <div className={styles.logo}>
                <h2>UbeU</h2>
                <button
                    className={styles.toggleBtn}
                    onClick={() => setIsCollapsed(!isCollapsed)}
                    aria-label={isCollapsed ? 'Expand sidebar' : 'Collapse sidebar'}
                >
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        {isCollapsed ? (
                            <path strokeLinecap="round" strokeLinejoin="round" d="M9 5l7 7-7 7" />
                        ) : (
                            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
                        )}
                    </svg>
                </button>
            </div>
            <nav className={styles.nav}>
                {navItems.map((item) => (
                    <Link key={item.href} href={item.href} className={styles.navItem} title={item.label}>
                        {isCollapsed ? item.label.charAt(0) : item.label}
                    </Link>
                ))}
            </nav>
            <div className={styles.footer}>
                {!isCollapsed && (
                    <div className={styles.user}>
                        <div className={styles.avatar}>HR</div>
                        <div className={styles.userInfo}>
                            <p className={styles.userName}>Hiring Manager</p>
                            <p className={styles.userRole}>Acme Corp</p>
                        </div>
                    </div>
                )}
                {isCollapsed && (
                    <div className={styles.avatarOnly}>
                        <div className={styles.avatar}>HR</div>
                    </div>
                )}
                <Link href="/login" className={styles.logoutBtn} title="Sign Out">
                    {isCollapsed ? '←' : 'Sign Out'}
                </Link>
            </div>
        </aside>
    );
}
