import Link from 'next/link';
import styles from './Sidebar.module.css';

const navItems = [
    { label: 'Dashboard', href: '/dashboard', icon: '📊' },
    { label: 'Assessments', href: '/dashboard/assessments', icon: '📝' },
    { label: 'Candidates', href: '/dashboard/candidates', icon: '👥' },
    { label: 'Settings', href: '/dashboard/settings', icon: '⚙️' },
];

export default function Sidebar() {
    return (
        <aside className={styles.sidebar}>
            <div className={styles.logo}>
                <h2>UbeU <span className={styles.role}>HR</span></h2>
            </div>
            <nav className={styles.nav}>
                {navItems.map((item) => (
                    <Link key={item.href} href={item.href} className={styles.navItem}>
                        <span className={styles.icon}>{item.icon}</span>
                        {item.label}
                    </Link>
                ))}
            </nav>
            <div className={styles.footer}>
                <div className={styles.user}>
                    <div className={styles.avatar}>HR</div>
                    <div className={styles.userInfo}>
                        <p className={styles.userName}>Hiring Manager</p>
                        <p className={styles.userRole}>Acme Corp</p>
                    </div>
                </div>
            </div>
        </aside>
    );
}
