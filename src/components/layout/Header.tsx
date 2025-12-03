'use client';

import { usePathname } from 'next/navigation';
import styles from './Header.module.css';

export default function Header({ title }: { title?: string }) {
    const pathname = usePathname();

    const getTitle = () => {
        if (title) return title;
        if (pathname.includes('/assessment')) return 'Assessments';
        if (pathname.includes('/candidates')) return 'Candidates';
        if (pathname.includes('/settings')) return 'Settings';
        return 'Dashboard';
    };

    return (
        <header className={styles.header}>
            <div className={styles.title}>
                <h1>{getTitle()}</h1>
            </div>
            <div className={styles.actions}>
                <button className={styles.iconBtn} aria-label="Notifications">
                    🔔
                </button>
                <button className={styles.iconBtn} aria-label="Help">
                    ❓
                </button>
            </div>
        </header>
    );
}
