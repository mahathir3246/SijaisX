import { Button, Panel, Badge, TagProps } from 'rsuite';
import "../../../../TeacherPage/TeacherDashboard.scss"
import { SubstitutionFE, SubstitutionBE } from './SubstituteJobsCard';
import { add_substitute_to_batch, cancel_application_for_batch } from '../../../../../functions/api_calls';
import { getUserID } from '../../../../../functions/auth';
import { useState } from 'react';
import JobDetails from '../Details/JobDetails';

export interface Props {
    substitution: SubstitutionFE;
    originalData: SubstitutionBE;
    onApply?: () => void;  // Callback to refresh the list after applying
}


type TagColour = NonNullable<TagProps['color']>;

const statusColour: Record<SubstitutionFE['status'], TagColour> = {
  Available: 'blue',
  Applied: 'orange',
  Accepted: 'green',
};

export const statusClass: Record<SubstitutionFE['status'], string> = {
  Available: 'job-card job-card--pending',
  Applied: 'job-card job-card--searching',
  Accepted: 'job-card job-card--accepted',
};

const ClassCard = ({ substitution, originalData, onApply }: Props) => {
    const [isApplying, setIsApplying] = useState(false);
    const [applied, setApplied] = useState(false);
    const [showPopup, setShowPopup] = useState(false);
    const [isWithdrawing, setIsWithdrawing] = useState(false);
    
    const handleApply = async (e: React.MouseEvent)=> {
        e.stopPropagation();
        const substituteID = getUserID();
        if (!substituteID) {
            alert('You must be logged in to apply');
            return;
        }

        setIsApplying(true);
        try {
            const result = await add_substitute_to_batch(substituteID, substitution.batch_ID);
            
            if (result && result.success) {
                setApplied(true);
                alert('Successfully applied for this job!');
                if (onApply) {
                    onApply();  // Refresh the list
                }
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

    return (
        <Panel bordered bodyFill className={statusClass[substitution.status]} onClick={() => setShowPopup(true)}>
            <div className="job-card__header">
                <Badge content={substitution.status} color={statusColour[substitution.status]} />
            </div>
            <h6>{substitution.date}</h6>
            <h6>{substitution.beginning_time} - {substitution.ending_time}</h6>
            <h6>{substitution.school_name}</h6>
            <h6>{substitution.teacher_name}</h6>
            <h6>{substitution.amount_of_hours}</h6>
            <span className="job-card__meta">{substitution.subject}</span>
            <span className="job-card__meta">{substitution.grade}</span>
                
                {/* Only show Apply button for jobs with 'searching' status */}
                {substitution.status === 'Available' && (
                    <>
                    <Button appearance="primary" block>
                        View Details
                    </Button>
                    <Button 
                        appearance="primary" 
                        onClick={handleApply}
                        loading={isApplying}
                        disabled={isApplying}
                    >
                        {isApplying ? 'Applying...' : 'Apply'}
                    </Button>
                    </>
                )}
                
                {substitution.status === 'Applied' && (
                    <>
                    <Button appearance="primary" block>
                        View Details
                    </Button>
                    <Button 
                        appearance="primary" 
                        disabled
                    >
                        Applied ✓
                    </Button>
                    <Button style={{backgroundColor: '#cb0d0d', color: 'white'}} block>
                        Withdraw Application
                    </Button>
                    </>
                )}
                {substitution.status === 'Accepted' && (
                    <>
                    <Button appearance="primary" block>
                        View Details
                    </Button>
                    <Button 
                        appearance="primary" 
                        disabled
                        
                    >
                        Assigned ✓
                    </Button>
                    <Button 
                    style={{backgroundColor: '#cb0d0d', color: 'white'}} 
                    block 
                    onClick={handleWithdraw} 
                    loading={isWithdrawing} 
                    disabled={isWithdrawing}>
                        Cancel Assignment
                    </Button>
                    </>
                )}
            <JobDetails
                open={showPopup}
                onClose={() => setShowPopup(false)}
                substitution={originalData}
                status={substitution.status}
            />
        </Panel>
    );
};

export default ClassCard;