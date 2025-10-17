import { Modal, Tag, Divider } from 'rsuite';
import { Assignment } from '../teacherUpcomings';
import styles from "../../../../scss_stylings/TeacherAssignmentPopup.module.scss";

export interface AssignmentDetailsModalProps {
    open: boolean;
    onClose: () => void;
    assignment: Assignment | null;
}


export default function AssignmentDetailsModal({ open, onClose, assignment }: AssignmentDetailsModalProps) {
    if (!assignment) return null;

    const formatDate = (dateString: string) => {
        const dateObj = new Date(dateString);
        const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
        const formattedDate = dateObj.toLocaleDateString('fi-FI');
        return `${formattedDate} ${dayOfWeek}`;
    };

    const formatTime = (timeString: string) => {
        return timeString.slice(11, 16);
    };

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