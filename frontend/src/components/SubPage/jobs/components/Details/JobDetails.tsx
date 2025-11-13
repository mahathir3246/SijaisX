import { Modal, Button, Divider } from 'rsuite';
import { SubstitutionBE } from '../Card/SubstituteJobsCard';
import styles from "../../../../../scss_stylings/TeacherAssignmentPopup.module.scss";
import { useState } from 'react';
import { getUserID } from '../../../../../functions/auth';
import { add_substitute_to_batch, cancel_application_for_batch } from '../../../../../functions/api_calls';
import "../../.././../TeacherPage/TeacherDashboard.scss"

export interface SubstitutionDetailsModalProps {
    open: boolean;
    onClose: () => void;
    substitution: SubstitutionBE;
    status: 'Available' | 'Applied' | 'Accepted';
}

export const statusClass: Record<SubstitutionBE['status'], string> = {
    Available: 'status-badge status-pending',
    Applied: 'status-badge status-searching',
    Accepted: 'status-badge status-accepted',
  };

export default function JobDetails({ open, onClose, substitution, status }: SubstitutionDetailsModalProps) {
    const [isApplying, setIsApplying] = useState(false);
    const [isWithdrawing, setIsWithdrawing] = useState(false);

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

    const handleWithdraw = async (e: React.MouseEvent) => {
            e.stopPropagation();
            const substituteID = getUserID();
            if (!substituteID) {
                alert('You must be logged in to withdraw');
                return;
            }
            try{
                console.log('withdraw', { substituteID, batchID: substitution.batch_ID });
                const result = await cancel_application_for_batch(substituteID, substitution.batch_ID);
                if (result && result.success) {
                    alert('Successfully withdrawn from this job!');
    
                } else {
                    alert(result?.error || 'Failed to withdraw from this job');
                }
            } catch (error) {
                console.error('Error withdrawing from job:', error);
                alert('An error occurred while withdrawing');
            } finally {
                setIsWithdrawing(false);
            }
    };

    if (!substitution) return null;
    
    return (
        <Modal size="lg" open={open} onClose={onClose} className="job-details-modal">
            <Modal.Header className="job-details-modal-header">
                <Modal.Title>Assignment Details</Modal.Title>
            </Modal.Header>

            <Modal.Body className="job-details-modal-body">
                <div className="job-details-content">
                    <div className="details-top-section">
                        <div className="date-info">
                            <h3 className="date-title">{formatDate(substitution.date)}</h3>
                            <h3 className="date-title">{substitution.teacher_name} </h3>
                            <h3 className="date-title">{substitution.school_name} </h3>
                        </div>
                        <span className={statusClass[status]}>
                            {status}
                        </span>
                    </div>

                    <Divider className={styles.divider} />

                    <div className="classes-section">
                        <h4 className="section-title">Classes ({substitution.classes.length})</h4>
                        <div className="classes-list">
                            {substitution.classes.map((cls, index) => (
                                <div key={index} className="class-card">
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
                                            <span className="info-value">{substitution.school_name}</span>
                                        </div>
                                    </div>
                                    <div className="time-section">
                                        <span className="info-label">Time:</span>
                                        <span className="info-value">
                                        {cls.beginning_time.slice(11, 16)} - {cls.ending_time.slice(11, 16)}
                                        </span>
                                    </div>
                                    <div className="info-item">
                                            <span className="info-label">Notes:</span>
                                            <span className="info-value">{cls.notes}</span>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    <Divider className={styles.divider} />

                    <div className="summary-section">
                        <h4 className="section-title">Summary</h4>
                        <div className="summary-grid">
                        <div className="summary-item">
                            <span className="summary-label">Total Classes:</span>
                            <span className="summary-value">{substitution.classes.length}</span>
                        </div>
                        <div className="summary-item">
                            <span className="summary-label">Time Range:</span>
                            <span className="summary-value">{substitution.classes[0].beginning_time.slice(11, 16)} - {substitution.classes[substitution.classes.length - 1].ending_time.slice(11, 16)}</span>
                        </div>
                        <div className="summary-item">
                            <span className="summary-label">Subjects:</span>
                            <span className="summary-value">{[...new Set(substitution.classes.map(c => c.subject))].join(', ')}</span>
                        </div>
                        <div className="summary-item">
                            <span className="summary-label">Grades:</span>
                            <span className="summary-value">{[...new Set(substitution.classes.map(c => c.subject))].join(', ')}</span>
                        </div>
                        </div>
                    </div>
                </div>
            </Modal.Body>

            <Modal.Footer className="job-details-modal-footer">
            <div className={styles.actions}>
                    {status === 'Available' && (
                        <button 
                            className={styles.applyButton} 
                            onClick={handleApply}
                            disabled={isApplying}
                            style={{ backgroundColor: '#28a745', color: 'white', marginRight: '10px' }}
                        >
                            {isApplying ? 'Applying...' : 'Apply'}
                        </button>
                    )}
                    {status === 'Applied' && (
                        <Button 
                            className="close-button"
                            style={{ backgroundColor: '#e74c3c', color: 'white', marginRight: '10px' }}
                        >
                            Cancel Application
                        </Button>
                    )}
                    {status === 'Accepted' && (
                        <Button 
                            className="close-button"
                            onClick={handleWithdraw}
                            style={{ backgroundColor: '#e74c3c', color: 'white', marginRight: '10px' }}
                        >
                            Cancel Assigment
                        </Button>
                    )}
                    <Button appearance="primary" className="close-button" 
                    onClick={(e) => {
                        e.stopPropagation();
                        onClose();                
                    }}>
                        Close
                    </Button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}