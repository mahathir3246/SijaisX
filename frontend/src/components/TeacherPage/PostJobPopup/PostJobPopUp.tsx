import { useState, useEffect, useCallback } from 'react';
import { Modal, Message, toaster, Button } from 'rsuite';
import ScheduleJobMode from './ScheduleJobMode';
import CustomJobs from './CustomClassForm';
import styles from "../../../scss_stylings/postJobPopup.module.scss"
import { getUserID } from '../../../functions/auth';
import { CustomJobData } from './CustomCLassCard';
import { create_batch_assignment, create_class, get_teacher_info } from '../../../functions/api_calls';
import { TeacherData } from '../MainContent/teacherProfile';



export interface Props { 
    open: boolean;
    onClose(): void;
}

export default function PostJobModal({ open, onClose }: Props) {
    // Add mode selection state
    const [mode, setMode] = useState<'schedule' | 'custom'>('schedule');
    // Keep teacher ID logic

    const teacherID = getUserID() || "";

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
                )}
            </Modal.Body>

            <Modal.Footer className={styles.footer}>
                <div className={styles.actions}>
                    <button className={styles.closeButton} onClick={onClose}>
                        Close
                    </button>
                    <Button
                        className={styles.saveButton}> 
                        Submit Assignment
                    </Button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}