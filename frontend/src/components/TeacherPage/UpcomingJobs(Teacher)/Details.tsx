import { Modal, Divider, Button } from 'rsuite';
import { Assignment } from './TeacherJobsHook';
import styles from "../../../scss_stylings/TeacherAssignmentPopup.module.scss";
import { useState, useEffect } from 'react';
import { getUserID } from '../../../functions/auth';
import { get_batch_of_assignment_volunteers } from '../../../functions/api_calls';
import VolunteerSelector from './Cards/VolunteerSelector';
import { delete_assignments } from '../../../functions/api_calls';

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

    const handleDelete = async () => {
        if (!assignment) return;
        
        const teacherID = getUserID();
        if (!teacherID) return;
        
        if (confirm('Delete this assignment?')) {
            const assignmentIds = assignment.classes.map(cls => cls.assignment_ID);
            await delete_assignments(teacherID, assignmentIds);
            onClose();
        }
    };


    if (!assignment) return null;
    
    return (
        <Modal size="lg" open={open} onClose={onClose} className="job-details-modal">
            <Modal.Header className="job-details-modal-header">
                <Modal.Title>Assignment Details</Modal.Title>
            </Modal.Header>

            <Modal.Body className="job-details-modal-body">
                <div className="job-details-content">
                    <div className="details-top-section">
                        <div className="date-info">
                            <h3 className="date-title">{formatDate(assignment.date)}</h3>
                        </div>
                        <span className={`status-badge status-${assignment.status}`}>
                            {assignment.status}
                        </span>
                    </div>

                    <Divider className={styles.divider} />

                    <div className="classes-section">
                        <h4 className="section-title">Classes ({assignment.classes.length})</h4>
                        <div className="classes-list">
                            {assignment.classes.map((cls) => (
                                <div key={cls.assignment_ID} className="class-card">
                                    <div className="class-info-grid">
                                        <div className="info-item">
                                            <span className="info-label">Subject:</span>
                                            <span className="info-value">{cls.subject}</span>
                                        </div>
                                        <div className="info-item">
                                            <span className="info-label">Grade:</span>
                                            <span className="info-value">{cls.grade}</span>
                                        </div>
                                        <div className="info-item">
                                            <span className="info-label">Room:</span>
                                            <span className="info-value">{cls.room}</span>
                                        </div>
                                        <div className="info-item">
                                            <span className="info-label">School:</span>
                                            <span className="info-value">{cls.school_name}</span>
                                        </div>
                                    </div>
                                    <div className="time-section">
                                        <span className="info-label">Time:</span>
                                        <span className="info-value">
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


                    <div className="summary-section">
                        <h4 className="section-title">Summary</h4>
                        <div className="summary-grid">
                        <div className="summary-item">
                            <span className="summary-label">Total Classes:</span>
                            <span className="summary-value">{assignment.classes.length}</span>
                        </div>
                        <div className="summary-item">
                            <span className="summary-label">Time Range:</span>
                            <span className="summary-value">{formatTime(assignment.classes[0].beginning_time)} - {formatTime(assignment.classes[assignment.classes.length - 1].ending_time)}</span>
                        </div>
                        <div className="summary-item">
                            <span className="summary-label">Subjects:</span>
                            <span className="summary-value">{[...new Set(assignment.classes.map(c => c.subject))].join(', ')}</span>
                        </div>
                        <div className="summary-item">
                            <span className="summary-label">Grades:</span>
                            <span className="summary-value">{[...new Set(assignment.classes.map(c => c.grade))].join(', ')}</span>
                        </div>
                        </div>
                    </div>
                </div>
            </Modal.Body>

            <Modal.Footer className="job-details-modal-footer">
                <div className={styles.actions}>
                    <Button 
                        className="close-button"
                        onClick={handleDelete}
                        style={{ backgroundColor: '#e74c3c', color: 'white', marginRight: '10px' }}
                    >
                        Delete Assignment
                    </Button>
                    <Button onClick={onClose} appearance="primary" className="close-button">
                      Close
                    </Button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}