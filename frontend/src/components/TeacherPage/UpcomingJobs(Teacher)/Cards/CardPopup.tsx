import { Modal, Tag, Divider, SelectPicker } from 'rsuite';
import { Assignment } from '../teacherUpcomings';
import styles from "../../../../scss_stylings/TeacherAssignmentPopup.module.scss";
import { useState, useEffect } from 'react';
import { getUserID } from '../../../../functions/auth';
import { get_batch_of_assignment_volunteers } from '../../../../functions/api_calls';
import VolunteerSelector from './VolunteerSelector';

export interface AssignmentDetailsModalProps {
    open: boolean;
    onClose: () => void;
    assignment: Assignment | null;
}

interface Volunteer {
    substitute_ID: string;
    name: string;
    email: string;
}

export default function AssignmentDetailsModal({ open, onClose, assignment }: AssignmentDetailsModalProps) {
    const [volunteers, setVolunteers] = useState<Volunteer[]>([]);
    const [loading, setLoading] = useState(false);

    const fetchVolunteers = async () => {
        if (!assignment) return;
        
        setLoading(true);
        try {
            const teacherID = getUserID();
            if (!teacherID) {
                throw new Error('No teacher ID found');
            }

            // Check if assignment has a batch_ID
            if (assignment.batch_ID) {
                // Use batch volunteers API
                const response = await get_batch_of_assignment_volunteers(assignment.batch_ID, teacherID);
                if (response && response.volunteers) {
                    setVolunteers(response.volunteers);
                }
            }
        } catch (error) {
            console.error('Error fetching volunteers:', error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (open && assignment && assignment.status === 'pending') {
            fetchVolunteers();
        }
    }, [open, assignment]);

    const formatDate = (dateString: string) => {
        const dateObj = new Date(dateString);
        const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
        const formattedDate = dateObj.toLocaleDateString('fi-FI');
        return `${formattedDate} ${dayOfWeek}`;
    };

    const formatTime = (timeString: string) => {
        return timeString.slice(11, 16);
    };

    if (!assignment) return null;
    
    return (
        <Modal size="lg" open={open} onClose={onClose} className={styles.modal}>
            <Modal.Header className={styles.header}>
                <h4>Assignment Details</h4>
            </Modal.Header>

            <Modal.Body className={styles.body}>
                <div className={styles.content}>
                    <div className={styles.headerSection}>
                        <h3 className={styles.dateTitle}>{formatDate(assignment.date)} </h3>
                        <Tag size="lg" className={styles.statusTag}>
                            {assignment.status}
                        </Tag>
                    </div>

                    <Divider className={styles.divider} />

                    <div className={styles.classesSection}>
                        <h4 className={styles.sectionTitle}>Classes ({assignment.classes.length})</h4>
                        <div className={styles.classesList}>
                            {assignment.classes.map((cls) => (
                                <div key={cls.assignment_ID} className={styles.classCard}>
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
                                            <span className={styles.infoValue}>{cls.school_name}</span>
                                        </div>
                                    </div>
                                    <div className={styles.timeInfo}>
                                        <span className={styles.infoLabel}>Time:</span>
                                        <span className={styles.infoValue}>
                                            {formatTime(cls.beginning_time)} - {formatTime(cls.ending_time)}
                                        </span>
                                    </div>
                                    {cls.substitute_name && (
                                        <div className={styles.substituteInfo}>
                                            <span className={styles.infoLabel}>Assigned Substitute:</span>
                                            <span className={styles.substituteName}>{cls.substitute_name}</span>
                                        </div>
                                    )}
                                    <div className={styles.notesInfo}>
                                        <span className={styles.infoLabel}>Notes:</span>
                                        <span className={styles.notesText}>{cls.notes}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                    {assignment.status === 'pending' && (
                        <>
                            <Divider className={styles.divider} />
                            <div className={styles.applicantsSection}>
                                <h4 className={styles.sectionTitle}>
                                    Applicants ({volunteers.length})
                                </h4>
                                
                                {loading ? (
                                    <div style={{ textAlign: 'center', padding: '20px' }}>
                                        Loading applicants...
                                    </div>
                                ) : (
                                    <div className={styles.applicantsList}>
                                        <VolunteerSelector 
                                            volunteers={volunteers}
                                            batchID={assignment.batch_ID || ''}
                                            onAcceptSuccess={onClose}
                                        />
                                    </div>
                                )}
                            </div>
                        </>
                    )}

                    <Divider className={styles.divider} />
                    <Divider className={styles.divider} />

                    <div className={styles.summarySection}>
                        <h4 className={styles.sectionTitle}>Summary</h4>
                        <div className={styles.summaryGrid}>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Total Classes:</span>
                                <span className={styles.summaryValue}>{assignment.classes.length}</span>
                            </div>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Time Range:</span>
                                <span className={styles.summaryValue}>
                                    {formatTime(assignment.classes[0].beginning_time)} - {formatTime(assignment.classes[assignment.classes.length - 1].ending_time)}
                                </span>
                            </div>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Subjects:</span>
                                <span className={styles.summaryValue}>
                                    {[...new Set(assignment.classes.map(c => c.subject))].join(', ')}
                                </span>
                            </div>
                            <div className={styles.summaryItem}>
                                <span className={styles.summaryLabel}>Grades:</span>
                                <span className={styles.summaryValue}>
                                    {[...new Set(assignment.classes.map(c => c.grade))].join(', ')}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </Modal.Body>

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