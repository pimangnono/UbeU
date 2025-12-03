import styles from './Header.module.css';

export default function Header({ title }: { title?: string }) {
    return (
        <header className={styles.header}>
            <div className={styles.title}>
                <h1>{title || 'Dashboard'}</h1>
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
