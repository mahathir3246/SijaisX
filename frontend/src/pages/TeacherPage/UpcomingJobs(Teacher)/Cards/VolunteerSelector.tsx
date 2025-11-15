import { SelectPicker, Button, Message, useToaster } from 'rsuite';
import { useState } from 'react';
import { update_batch_status } from '../../../../functions/api_calls';
import { getUserID } from '../../../../functions/auth';

interface Volunteer {
    substitute_ID: string;
    name: string;
    email: string;
}

interface VolunteerSelectorProps {
    volunteers: Volunteer[];
    batchID: string;
    onAcceptSuccess?: () => void;
}

export default function VolunteerSelector({ volunteers, batchID, onAcceptSuccess }: VolunteerSelectorProps) {
    const [selectedVolunteer, setSelectedVolunteer] = useState<string | null>(null);
    const [isAccepting, setIsAccepting] = useState(false);
    const toaster = useToaster();

    const handleAccept = async () => {
        if (!selectedVolunteer) {
            toaster.push(
                <Message showIcon type="warning">
                    Please select a substitute first
                </Message>,
                { placement: 'topCenter', duration: 3000 }
            );
            return;
        }

        const teacherID = getUserID();
        if (!teacherID) {
            toaster.push(
                <Message showIcon type="error">
                    Teacher ID not found. Please log in again.
                </Message>,
                { placement: 'topCenter', duration: 3000 }
            );
            return;
        }

        setIsAccepting(true);
        try {
            const response = await update_batch_status(batchID, {
                teacher_ID: teacherID,
                status: 'accepted',
                substitute_ID: selectedVolunteer
            });

            if (response) {
                toaster.push(
                    <Message showIcon type="success">
                        Substitute accepted successfully!
                    </Message>,
                    { placement: 'topCenter', duration: 3000 }
                );
                
                // Call the success callback to refresh the data
                if (onAcceptSuccess) {
                    onAcceptSuccess();
                }
            } else {
                throw new Error('Failed to update batch status');
            }
        } catch (error) {
            console.error('Error accepting substitute:', error);
            toaster.push(
                <Message showIcon type="error">
                    Failed to accept substitute. Please try again.
                </Message>,
                { placement: 'topCenter', duration: 3000 }
            );
        } finally {
            setIsAccepting(false);
        }
    };

    if (volunteers.length === 0) {
        return (
            <div style={{ 
                textAlign: 'center', 
                padding: '20px',
                fontStyle: 'italic',
                color: '#666'
            }}>
                No applicants yet
            </div>
        );
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
                <label style={{ 
                    display: 'block', 
                    marginBottom: '8px', 
                    fontWeight: '600',
                    fontSize: '14px'
                }}>
                    Available substitutes:
                </label>
                <SelectPicker
                    data={volunteers.map(vol => ({
                        label: `${vol.name} (${vol.email})`,
                        value: vol.substitute_ID
                    }))}
                    value={selectedVolunteer}
                    onChange={setSelectedVolunteer}
                    placeholder="Choose a substitute..."
                    style={{ width: '100%' }}
                    disabled={isAccepting}
                />
            </div>
            
            <Button 
                appearance="primary" 
                onClick={handleAccept}
                disabled={!selectedVolunteer || isAccepting}
                loading={isAccepting}
                style={{ 
                    width: '100%',
                    padding: '10px 0'
                }}
            >
                {isAccepting ? 'Accepting...' : 'Accept Substitute'}
            </Button>
        </div>
    );
}