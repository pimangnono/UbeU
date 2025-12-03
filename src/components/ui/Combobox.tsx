'use client';

import { useState, useEffect, useRef } from 'react';
import styles from './Combobox.module.css';

interface Option {
    id: string;
    label: string;
}

interface ComboboxProps {
    options: Option[];
    value: string;
    onChange: (value: string, isCustom?: boolean) => void;
    placeholder?: string;
    disabled?: boolean;
    label: string;
}

export default function Combobox({
    options,
    value,
    onChange,
    placeholder = 'Select...',
    disabled = false,
    label,
}: ComboboxProps) {
    const [isOpen, setIsOpen] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const [selectedLabel, setSelectedLabel] = useState('');
    const containerRef = useRef<HTMLDivElement>(null);

    // Update internal state when external value changes
    useEffect(() => {
        const option = options.find((o) => o.id === value);
        if (option) {
            setSelectedLabel(option.label);
            setSearchTerm(option.label);
        } else if (value) {
            // Custom value
            setSelectedLabel(value);
            setSearchTerm(value);
        } else {
            setSelectedLabel('');
            setSearchTerm('');
        }
    }, [value, options]);

    // Close dropdown when clicking outside
    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
                setIsOpen(false);
                // Reset search term to selected label if closed without selection
                if (selectedLabel) {
                    setSearchTerm(selectedLabel);
                } else {
                    setSearchTerm('');
                }
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, [selectedLabel]);

    const filteredOptions = options.filter((option) => {
        // If the search term matches the selected label exactly, show all options
        // This allows the user to see the full list when clicking the input after selection
        if (selectedLabel && searchTerm === selectedLabel) {
            return true;
        }
        return option.label.toLowerCase().includes(searchTerm.toLowerCase());
    });

    const handleSelect = (option: Option) => {
        onChange(option.id, false);
        setSelectedLabel(option.label);
        setSearchTerm(option.label);
        setIsOpen(false);
    };

    const handleCustomSelect = () => {
        onChange(searchTerm, true);
        setSelectedLabel(searchTerm);
        setIsOpen(false);
    };

    return (
        <div className={styles.container} ref={containerRef}>
            <label className={styles.label}>{label}</label>
            <div className={styles.inputWrapper}>
                <input
                    type="text"
                    className={styles.input}
                    placeholder={placeholder}
                    value={searchTerm}
                    onChange={(e) => {
                        setSearchTerm(e.target.value);
                        setIsOpen(true);
                    }}
                    onFocus={() => setIsOpen(true)}
                    disabled={disabled}
                />
                <span className={styles.arrow}>{isOpen ? '▲' : '▼'}</span>
            </div>

            {isOpen && !disabled && (
                <div className={styles.dropdown}>
                    {filteredOptions.length > 0 ? (
                        filteredOptions.map((option) => (
                            <button
                                key={option.id}
                                className={`${styles.option} ${value === option.id ? styles.selected : ''}`}
                                onClick={() => handleSelect(option)}
                            >
                                {option.label}
                            </button>
                        ))
                    ) : (
                        <div className={styles.noResults}>No matching options</div>
                    )}

                    {searchTerm && !filteredOptions.find(o => o.label.toLowerCase() === searchTerm.toLowerCase()) && (
                        <button className={`${styles.option} ${styles.createOption}`} onClick={handleCustomSelect}>
                            + Create "{searchTerm}"
                        </button>
                    )}
                </div>
            )}
        </div>
    );
}
