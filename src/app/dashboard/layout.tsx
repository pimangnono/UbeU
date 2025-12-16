'use client';

import Sidebar from '@/components/layout/Sidebar';
import Header from '@/components/layout/Header';
import { SidebarProvider, useSidebar } from '@/components/layout/SidebarContext';
import styles from './layout.module.css';

function DashboardContent({ children }: { children: React.ReactNode }) {
    const { isCollapsed } = useSidebar();

    return (
        <div className={styles.container}>
            <Sidebar />
            <div
                className={styles.mainContent}
                style={{ marginLeft: isCollapsed ? '70px' : 'var(--sidebar-width)' }}
            >
                <Header />
                <main className={styles.pageContent}>
                    {children}
                </main>
            </div>
        </div>
    );
}

export default function DashboardLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <SidebarProvider>
            <DashboardContent>{children}</DashboardContent>
        </SidebarProvider>
    );
}
