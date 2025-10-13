import { useState, useEffect } from 'react';
import { Modal } from 'rsuite';
import ScheduleJobMode from './ScheduleJobMode';
import styles from "../../../scss_stylings/postJobPopup.module.scss"


export interface Props { 
    open: boolean;
    onClose(): void;
}

export default function PostJobModal({ open, onClose }: Props) {
    // Add mode selection state
    const [mode, setMode] = useState<'schedule' | 'custom'>('schedule');
    // Keep teacher ID logic

    // Reset state when modal opens/closes
    useEffect(() => {
        if (!open) {
            setMode('schedule');
        }
    }, [open]);


    // Handle mode change
    const handleModeChange = (newMode: 'schedule' | 'custom') => {
        setMode(newMode);
    };

    return (
        <Modal size="lg" open={open} onClose={onClose} className={styles.modal}>
            <Modal.Header className={styles.header}>
                <h4>Post a Job</h4>
            </Modal.Header>

            <Modal.Body className={styles.body}>
                {/* Add your mode selection UI here */}
                <div className={styles.modeSelection}>
                    <button 
                        className={`${styles.modeButton} ${mode === 'schedule' ? styles.activeMode : styles.inactiveMode}`}
                        onClick={() => handleModeChange('schedule')}
                    >
                        📅 Use My Schedule
                    </button>
                    <button 
                        className={`${styles.modeButton} ${mode === 'custom' ? styles.activeMode : styles.inactiveMode}`}
                        onClick={() => handleModeChange('custom')}
                    >
                        ✏️ Create Custom Job
                    </button>
                </div>

                {/* Mode Content */}
                {mode === 'schedule' && (
                    <ScheduleJobMode/>
                )}

                {mode === 'custom' && (
                    <div>Coming</div>
                )}            </Modal.Body>

            <Modal.Footer className={styles.footer}>
                <div className={styles.actions}>
                    <button className={styles.closeButton} onClick={onClose}>
                        Close
                    </button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}