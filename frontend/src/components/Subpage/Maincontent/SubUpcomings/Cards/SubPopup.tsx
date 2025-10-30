import { Modal, Tag, Divider } from 'rsuite';
import { SubstitutionBE } from '../SubstituteJobLists';
import styles from "../../../../../scss_stylings/TeacherAssignmentPopup.module.scss";
import { useState } from 'react';
import { getUserID } from '../../../../../functions/auth';
import { add_substitute_to_batch } from '../../../../../functions/api_calls';

export interface SubstitutionDetailsModalProps {
    open: boolean;
    onClose: () => void;
    substitution: SubstitutionBE | null;
    status: 'searching' | 'pending' | 'accepted';
}

export default function SubstitutionDetailsModal({ open, onClose, substitution, status }: SubstitutionDetailsModalProps) {
    const [isApplying, setIsApplying] = useState(false);

    const formatDate = (dateString: string) => {
        const dateObj = new Date(dateString);
        const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
        const formattedDate = dateObj.toLocaleDateString('fi-FI');
        return `${formattedDate} ${dayOfWeek}`;
    };

    const handleApply = async () => {
        if (!substitution) return;
        
        const substituteID = getUserID();
        if (!substituteID) return;
        
        setIsApplying(true);
        try {
            const result = await add_substitute_to_batch(substituteID, substitution.batch_ID);
            
            if (result && result.success) {
                alert('Successfully applied for this job!');
                onClose();
            } else {
                alert(result?.error || 'Failed to apply for this job');
            }
        } catch (error) {
            console.error('Error applying for job:', error);
            alert('An error occurred while applying');
        } finally {
            setIsApplying(false);
        }
    };

    if (!substitution) return null;
    
    return (
        <Modal size="lg" open={open} onClose={onClose} className={styles.modal}>
            <Modal.Header className={styles.header}>
                <h4>Job Details</h4>
            </Modal.Header>

            <Modal.Body className={styles.body}>
                <div className={styles.content}>
                    <div className={styles.headerSection}>
                        <h3 className={styles.dateTitle}>{formatDate(substitution.date)} </h3>
                        <Tag size="lg" className={styles.statusTag}>
                            {status}
                        </Tag>
                    </div>

                    <Divider className={styles.divider} />

                    <div className={styles.classesSection}>
                        <h4 className={styles.sectionTitle}>Classes ({substitution.classes.length})</h4>
                        <div className={styles.classesList}>
                            {substitution.classes.map((cls, index) => (
                                <div key={index} className={styles.classCard}>
                                    <div className={styles.classInfo}>
                                        <div className={styles.infoRow}>
                                            <span className={styles.infoLabel}>Subject:</span>
                                            <span className={styles.infoValue}>{cls.subject}</span>
                                        </div>
                                        <div className={styles.infoRow}>
                                            <span className={styles.infoLabel}>Grade:</span>
                                            <span className={styles.infoValue}>{cls.grade}</span>
                                        </div>
                                        <div className={styles.infoRow}>
                                            <span className={styles.infoLabel}>Room:</span>
                                            <span className={styles.infoValue}>{cls.room}</span>
                                        </div>
                                        <div className={styles.infoRow}>
                                            <span className={styles.infoLabel}>School:</span>
                                            <span className={styles.infoValue}>{substitution.school_name}</span>
                                        </div>
                                    </div>
                                    <div className={styles.timeInfo}>
                                        <span className={styles.infoLabel}>Time:</span>
                                        <span className={styles.infoValue}>
                                            {cls.beginning_time.slice(11, 16)} - {cls.ending_time.slice(11, 16)}
                                        </span>
                                    </div>
                                    <div className={styles.notesInfo}>
                                        <span className={styles.infoLabel}>Notes:</span>
                                        <span className={styles.notesText}>{cls.notes}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    <Divider className={styles.divider} />

                    <div className={styles.summarySection}>
                        <h4 className={styles.sectionTitle}>Summary</h4>
                        <div className={styles.summaryGrid}>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Total Classes:</span>
                                <span className={styles.summaryValue}>{substitution.classes.length}</span>
                            </div>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Time Range:</span>
                                <span className={styles.summaryValue}>
                                    {substitution.classes[0].beginning_time.slice(11, 16)} - {substitution.classes[substitution.classes.length - 1].ending_time.slice(11, 16)}
                                </span>
                            </div>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Subjects:</span>
                                <span className={styles.summaryValue}>
                                    {[...new Set(substitution.classes.map(c => c.subject))].join(', ')}
                                </span>
                            </div>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Grades:</span>
                                <span className={styles.summaryValue}>
                                    {[...new Set(substitution.classes.map(c => c.grade))].join(', ')}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </Modal.Body>

            <Modal.Footer className={styles.footer}>
                <div className={styles.actions}>
                    {status === 'searching' && (
                        <button 
                            className={styles.applyButton} 
                            onClick={handleApply}
                            disabled={isApplying}
                            style={{ backgroundColor: '#28a745', color: 'white', marginRight: '10px' }}
                        >
                            {isApplying ? 'Applying...' : 'Apply'}
                        </button>
                    )}
                        <button className={styles.closeButton} onClick={(e) => {
                            e.stopPropagation();
                            onClose();
                        }}>
                            Close
                    </button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}