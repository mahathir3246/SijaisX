import { useState, useEffect } from 'react';
import { Message, Modal, toaster } from 'rsuite';
import ScheduleJobMode from './ScheduleJobMode';
import"./PostJob.scss"


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

    const handleSubmitSuccess = () => {
        toaster.push(<Message type="success">Job posted successfully!</Message>);
        onClose();
    };

    const handleSubmitError = (message: string) => {
        toaster.push(<Message type="error">{message}</Message>);
    };
    return (
        <Modal size="lg" open={open} onClose={onClose} className="post-job-modal">
            <Modal.Header className="post-job-modal__header">
                <h4>Post a Job</h4>
            </Modal.Header>

            <Modal.Body className="post-job-modal__body">
                <div className="mode-selection">
                    <button 
                        className={`mode-button ${mode === 'schedule' ? 'mode-button--active' : 'mode-button--inactive'}`}
                        onClick={() => handleModeChange('schedule')}
                    >
                        📅 Use My Schedule
                    </button>
                    <button 
                        className={`mode-button ${mode === 'custom' ? 'mode-button--active' : 'mode-button--inactive'}`}
                        onClick={() => handleModeChange('custom')}
                    >
                        ✏️ Create Custom Job
                    </button>
                </div>

                {mode === 'schedule' && (
                    <ScheduleJobMode onSubmitSuccess={handleSubmitSuccess} onSubmitError={handleSubmitError} />
                )}

                {mode === 'custom' && (
                    <div className="empty-state">
                        <p>Custom job creation coming soon...</p>
                    </div>
                )}
            </Modal.Body>

            <Modal.Footer className="post-job-modal__footer">
                <button className="close-button" onClick={onClose}>
                    Close
                </button>
            </Modal.Footer>
        </Modal>
    );
}