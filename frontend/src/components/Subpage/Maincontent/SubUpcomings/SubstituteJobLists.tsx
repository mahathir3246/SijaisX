
import '../../../../scss_stylings/card.module.scss';
import { useState,useEffect } from 'react';
import { getUserID } from '../../../../functions/auth';
import styles from "../../../../scss_stylings/card.module.scss";
import ClassCard from './Cards/ClassCard';
import { Loader} from 'rsuite';
import { get_batch_of_assignments_for_substitute, get_batch_of_available_assignments_for_substitute, get_all_applied_batches_of_substitute } from '../../../../functions/api_calls';

//This is the way data comes in from backend
export interface SubstitutionBE{
    classes: {
        beginning_time: string,
        duration: number,
        ending_time: string,
        grade: string,
        notes: string,
        room: string,
        subject: string,
        teacher_mail: string,
        teacher_name: string
    }[];
    date: string;
    school_name: string,
    teacher_email: string,
    teacher_name: string,
    batch_ID: string
}


//These are the data I want to show in UI

export interface SubstitutionFE{
    date: string,
    school_name: string,
    beginning_time: string,
    ending_time: string,
    amount_of_hours: string,
    grade: string,
    subject: string,
    teacher_name: string,
    status: 'searching' | 'pending' | 'accepted',
    batch_ID: string
}

export function cardContents(SubstitutionList: SubstitutionBE[], status: 'searching' | 'pending' | 'accepted'): SubstitutionFE[]{
    return SubstitutionList
        .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()).map(substitution =>{
        const school = substitution.school_name
        const dateObj = new Date(substitution.date);
        const dayOfWeek= dateObj.toLocaleDateString("en-US", {weekday: "long"});
        const formattedDate= dateObj.toLocaleDateString("fi-FI");
        const date= `${formattedDate} ${dayOfWeek}`;
        const beginning_time= substitution.classes[0].beginning_time.slice(11,16);
        const ending_time= substitution.classes[substitution.classes.length-1].ending_time.slice(11,16);
        const hours= `${substitution.classes.length} classes`
        const grade= [...new Set(substitution.classes.map(cls=>cls.grade))].join(",");
        const subject = [...new Set(substitution.classes.map(cls=> cls.subject))].join(",")
        const teacher = substitution.teacher_name;
        return{
            date:date,
            school_name:school,
            beginning_time:beginning_time,
            ending_time:ending_time,
            amount_of_hours:hours,
            grade: grade,
            subject: subject,
            teacher_name: teacher,
            status: status,
            batch_ID: substitution.batch_ID

        }
    })
}


interface SubUpcomingsProps{
    apiFunction?: (subID:string) => Promise<any>;
}
const SubstituteJobLists = ({ apiFunction = get_batch_of_available_assignments_for_substitute }: SubUpcomingsProps) => {
    const [substitutions, setSubstitutions] = useState<SubstitutionFE[]>([])
    const [originalData, setOriginalData] = useState<SubstitutionBE[]>([])
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const subID = getUserID()

    const fetchAvailableSubs = async () => {
        try{
            if (!subID) {
                setError('No Substitute ID found');
                setLoading(false);
                return;
            }
            
            const response = await apiFunction(subID)

            if (response && response.success){
                let status: 'searching' | 'pending' | 'accepted' = 'pending';
                
                if(apiFunction === get_batch_of_available_assignments_for_substitute){
                    status = 'searching'
                }else if(apiFunction === get_batch_of_assignments_for_substitute){
                    status = 'accepted'
                }else if(apiFunction === get_all_applied_batches_of_substitute){
                    status = 'pending'
                }
                const processed = cardContents(response.batches, status);
                setSubstitutions(processed)
                setOriginalData(response.batches)
            }else{
                setError('Failed to fetch Substitutions');
            }
        }catch(error){
            setError(`Error: ${error}`)
        }finally {
            setLoading(false);
        }
    }

    useEffect(()=>{
        fetchAvailableSubs()
    },[apiFunction])

    const handleApply = () => {
        // Refresh the list after successful application
        setLoading(true);
        fetchAvailableSubs();
    };

    if (loading) {
        return <Loader size="lg" center />;
    }

    return (
        <div>
            <div className={`${styles.galleryWrapper} ${styles.substituteCardRail}`}>  
                <div className={styles.substituteCardContainer}>
                    {substitutions.map((substitution, index) => (
                        <div
                            key={`${substitution.date}-${substitution.school_name}-${substitution.teacher_name}-${index}`}
                            className={styles.cardWrapper}
                        >
                            <ClassCard 
                                substitution={substitution}
                                originalData={originalData[index]}
                                onApply={handleApply} />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default SubstituteJobLists;