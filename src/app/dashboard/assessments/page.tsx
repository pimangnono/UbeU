'use client';

import { useState, useMemo } from 'react';
import Link from 'next/link';
import styles from './assessments.module.css';

// Mock assessment data
const mockAssessments = [
    {
        id: '1',
        title: 'Daily Coffee Consumption in Singapore',
        track: 'Data Analytics',
        category: 'Problem-Solving / Analytical',
        subcategory: 'Guesstimation',
        status: 'opened',
        assigned: ['Alex Johnson', 'Sarah Lee'],
        createdAt: '2024-12-10',
        difficulty: 'Fresh Graduate'
    },
    {
        id: '2',
        title: 'E-commerce Platform Strategy',
        track: 'Business Development',
        category: 'Case-Based',
        subcategory: 'Business Case Study',
        status: 'opened',
        assigned: ['Mike Chen', 'Emma Davis'],
        createdAt: '2024-12-08',
        difficulty: 'Senior'
    },
    {
        id: '3',
        title: 'Team Conflict Resolution',
        track: 'Human Resources',
        category: 'Behavioural / Soft-Skill',
        subcategory: 'Conflict Management',
        status: 'closed',
        assigned: ['John Smith'],
        createdAt: '2024-12-05',
        difficulty: 'Junior'
    },
    {
        id: '4',
        title: 'Product Feature Pitch',
        track: 'Product Management',
        category: 'Communication',
        subcategory: 'Structured Presentation / Pitch',
        status: 'inactive',
        assigned: [],
        createdAt: '2024-12-01',
        difficulty: 'Fresh Graduate'
    },
    {
        id: '5',
        title: 'Market Sizing: Cloud Storage',
        track: 'Data Analytics',
        category: 'Problem-Solving / Analytical',
        subcategory: 'Market Sizing',
        status: 'opened',
        assigned: ['Lisa Wang', 'Tom Brown', 'Amy Clark'],
        createdAt: '2024-12-12',
        difficulty: 'Expert'
    },
    {
        id: '6',
        title: 'Innovation Brainstorm Session',
        track: 'Research & Development',
        category: 'Creative / Innovation',
        subcategory: 'Brainstorming Challenge',
        status: 'opened',
        assigned: ['David Kim'],
        createdAt: '2024-12-11',
        difficulty: 'Junior'
    },
    {
        id: '7',
        title: 'Customer Journey Optimization',
        track: 'Marketing',
        category: 'Case-Based',
        subcategory: 'Customer Experience Case',
        status: 'inactive',
        assigned: ['Rachel Green'],
        createdAt: '2024-11-28',
        difficulty: 'Senior'
    },
];

// Get unique values for filters
const getUniqueValues = (key: keyof typeof mockAssessments[0]) => {
    const values = mockAssessments.map(a => a[key]);
    if (Array.isArray(values[0])) {
        return [...new Set(values.flat() as string[])].filter(Boolean);
    }
    return [...new Set(values as string[])].filter(Boolean);
};

const tracks = getUniqueValues('track') as string[];
const categories = getUniqueValues('category') as string[];
const subcategories = getUniqueValues('subcategory') as string[];
const statuses = ['opened', 'inactive', 'closed'];

export default function AssessmentsPage() {
    const [filters, setFilters] = useState({
        track: '',
        category: '',
        subcategory: '',
        status: '',
        search: ''
    });

    const filteredAssessments = useMemo(() => {
        return mockAssessments.filter(assessment => {
            if (filters.track && assessment.track !== filters.track) return false;
            if (filters.category && assessment.category !== filters.category) return false;
            if (filters.subcategory && assessment.subcategory !== filters.subcategory) return false;
            if (filters.status && assessment.status !== filters.status) return false;
            if (filters.search) {
                const search = filters.search.toLowerCase();
                return (
                    assessment.title.toLowerCase().includes(search) ||
                    assessment.assigned.some(a => a.toLowerCase().includes(search))
                );
            }
            return true;
        });
    }, [filters]);

    const clearFilters = () => {
        setFilters({
            track: '',
            category: '',
            subcategory: '',
            status: '',
            search: ''
        });
    };

    const getStatusClass = (status: string) => {
        switch (status) {
            case 'opened': return styles.statusOpened;
            case 'inactive': return styles.statusInactive;
            case 'closed': return styles.statusClosed;
            default: return '';
        }
    };

    return (
        <div className={styles.container}>
            <header className={styles.header}>
                <div className={styles.headerContent}>
                    <h1>Assessments</h1>
                    <p>Manage and track all your interview assessments</p>
                </div>
                <Link href="/dashboard/assessment/create" className={styles.createBtn}>
                    + Create New
                </Link>
            </header>

            {/* Filters Section */}
            <div className={styles.filtersSection}>
                <div className={styles.searchBox}>
                    <svg className={styles.searchIcon} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <circle cx="11" cy="11" r="8" />
                        <path d="m21 21-4.35-4.35" />
                    </svg>
                    <input
                        type="text"
                        placeholder="Search by title or candidate..."
                        value={filters.search}
                        onChange={(e) => setFilters(prev => ({ ...prev, search: e.target.value }))}
                        className={styles.searchInput}
                    />
                </div>

                <div className={styles.filterRow}>
                    <select
                        value={filters.track}
                        onChange={(e) => setFilters(prev => ({ ...prev, track: e.target.value }))}
                        className={styles.filterSelect}
                    >
                        <option value="">All Tracks</option>
                        {tracks.map(track => (
                            <option key={track} value={track}>{track}</option>
                        ))}
                    </select>

                    <select
                        value={filters.category}
                        onChange={(e) => setFilters(prev => ({ ...prev, category: e.target.value }))}
                        className={styles.filterSelect}
                    >
                        <option value="">All Categories</option>
                        {categories.map(cat => (
                            <option key={cat} value={cat}>{cat}</option>
                        ))}
                    </select>

                    <select
                        value={filters.subcategory}
                        onChange={(e) => setFilters(prev => ({ ...prev, subcategory: e.target.value }))}
                        className={styles.filterSelect}
                    >
                        <option value="">All Subcategories</option>
                        {subcategories.map(sub => (
                            <option key={sub} value={sub}>{sub}</option>
                        ))}
                    </select>

                    <select
                        value={filters.status}
                        onChange={(e) => setFilters(prev => ({ ...prev, status: e.target.value }))}
                        className={styles.filterSelect}
                    >
                        <option value="">All Statuses</option>
                        {statuses.map(status => (
                            <option key={status} value={status}>
                                {status.charAt(0).toUpperCase() + status.slice(1)}
                            </option>
                        ))}
                    </select>

                    {(filters.track || filters.category || filters.subcategory || filters.status || filters.search) && (
                        <button onClick={clearFilters} className={styles.clearBtn}>
                            Clear Filters
                        </button>
                    )}
                </div>
            </div>

            {/* Results Count */}
            <div className={styles.resultsInfo}>
                Showing <strong>{filteredAssessments.length}</strong> of {mockAssessments.length} assessments
            </div>

            {/* Assessments Table */}
            <div className={styles.tableContainer}>
                <table className={styles.table}>
                    <thead>
                        <tr>
                            <th>Assessment</th>
                            <th>Track</th>
                            <th>Category</th>
                            <th>Subcategory</th>
                            <th>Status</th>
                            <th>Assigned</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredAssessments.map(assessment => (
                            <tr key={assessment.id}>
                                <td>
                                    <div className={styles.assessmentTitle}>
                                        <span className={styles.title}>{assessment.title}</span>
                                        <span className={styles.meta}>
                                            {assessment.difficulty} • Created {assessment.createdAt}
                                        </span>
                                    </div>
                                </td>
                                <td>
                                    <span className={styles.trackBadge}>{assessment.track}</span>
                                </td>
                                <td>{assessment.category}</td>
                                <td>{assessment.subcategory}</td>
                                <td>
                                    <span className={`${styles.statusBadge} ${getStatusClass(assessment.status)}`}>
                                        {assessment.status}
                                    </span>
                                </td>
                                <td>
                                    {assessment.assigned.length > 0 ? (
                                        <div className={styles.assignedList}>
                                            {assessment.assigned.slice(0, 2).map((name, i) => (
                                                <span key={i} className={styles.assignedBadge}>{name}</span>
                                            ))}
                                            {assessment.assigned.length > 2 && (
                                                <span className={styles.moreCount}>
                                                    +{assessment.assigned.length - 2}
                                                </span>
                                            )}
                                        </div>
                                    ) : (
                                        <span className={styles.noAssigned}>No candidates</span>
                                    )}
                                </td>
                                <td>
                                    <div className={styles.actions}>
                                        <Link
                                            href={`/dashboard/assessment/${assessment.id}`}
                                            className={styles.actionLink}
                                        >
                                            View
                                        </Link>
                                        <button className={styles.actionBtn}>Edit</button>
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>

                {filteredAssessments.length === 0 && (
                    <div className={styles.emptyState}>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                            <path d="M9 12h6m-3-3v6m-7 4h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                        </svg>
                        <h3>No assessments found</h3>
                        <p>Try adjusting your filters or create a new assessment</p>
                    </div>
                )}
            </div>
        </div>
    );
}
