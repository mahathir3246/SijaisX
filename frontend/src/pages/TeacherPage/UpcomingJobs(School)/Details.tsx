import { Modal, Divider, Button } from 'rsuite';
import { SchoolAssignment } from './SchoolJobHook';
import "../TeacherDashboard.scss"

export interface SchoolAssignmentDetailsModalProps {
    open: boolean;
    onClose: () => void;
    assignment: SchoolAssignment | null;
}


export default function SchoolAssignmentDetailsModal({ open, onClose, assignment }: SchoolAssignmentDetailsModalProps) {
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
        <Modal size="lg" open={open} onClose={onClose} className="job-details-modal">
            <Modal.Header className="job-details-modal-header">
                <Modal.Title>Assignment Details</Modal.Title>
            </Modal.Header>

            <Modal.Body className="job-details-modal-body">
                <div className="job-details-content">
                    <div className="details-top-section">
                        <div className="date-info">
                            <h3 className="date-title">{formatDate(assignment.date)}</h3>
                            <h3 className="date-title">{assignment.classes[0].teacher_name} </h3>
                        </div>
                        <span className={`status-badge status-${assignment.status}`}>
                            {assignment.status}
                        </span>
                    </div>

                    <Divider className="divider" />

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
                                        <div className="substituteInfo">
                                            <span className="infoLabel">Assigned Substitute:</span>
                                            <span className="substituteName">{cls.substitute_name}</span>
                                        </div>
                                    )}
                                </div>
                            ))}
                        </div>
                    </div>

                    <Divider className="divider"/>

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
                <Button onClick={onClose} appearance="primary" className="close-button">
                Close
                </Button>
            </Modal.Footer>
        </Modal>
    );
}