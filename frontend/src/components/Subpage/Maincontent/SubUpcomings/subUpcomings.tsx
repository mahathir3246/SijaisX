
import '../../../../scss_stylings/card.module.scss';
import { useState,useEffect } from 'react';
import { getUserID } from '../../../../functions/auth';
import SubUpcomingsCardGallery from './Cards/SubUpcomingsCardGallery';
import { get_batch_of_available_assignments_for_substitute } from '../../../../functions/api_calls';
import { Loader} from 'rsuite';

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
    teacher_name: string
}


//These are the data I want to show in UI

export interface SubstitutionFE{
    date: string,//date
    school_name: string,//school
    beginning_time: string,//
    ending_time: string,//
    amount_of_hours: string,//
    grade: string,//
    subject: string,//
    teacher_name: string,
}

export function cardContents(SubstitutionList: SubstitutionBE[]): SubstitutionFE[]{
    return SubstitutionList.map(substitution =>{
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
            teacher_name: teacher

        }
    })
}
const SubUpcomings = () => {

    const [substitutions, setSubstitutions] = useState<SubstitutionFE[]>([])
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);


    const subID = getUserID()

    useEffect(()=>{
        const fetchAvailableSubs = async () =>{
            try{
                if (!subID) {
                    setError('No Substitute ID found');
                    setLoading(false);
                    return;
                }
                
                const response = await get_batch_of_available_assignments_for_substitute(subID)

                if (response && response.success){
                    const processed = cardContents(response.batches);
                    setSubstitutions(processed)
                }else{
                    setError('Failed to fetch Substitutions');
                }
            }catch(error){
                setError("Error")
            }finally {
                setLoading(false);
            }
     }
     fetchAvailableSubs()
    
    },[])

    if (loading) {
        return <Loader size="lg" center />;
    }

    return (
        <div>
            <SubUpcomingsCardGallery substitutions={substitutions} />
        </div>
    );

};



export default SubUpcomings;
