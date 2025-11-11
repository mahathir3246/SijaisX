
import { useState , useEffect} from 'react';
import styles from '../../../scss_stylings/card.module.scss';
import SchoolAssignmentDetailsModal from './SchoolCardPopup';
import { getUserID } from '../../../functions/auth';
import { get_all_assignments_of_school, get_teacher_info } from '../../../functions/api_calls';
import { TeacherData } from '../TeacherProfile/TeacherProfile';
import SchoolJobsCard from './SchoolJobsCard';

export interface SchoolAssignment {
  date: string;
  classes: {
    assignment_ID: string;
    subject: string;
    grade: string;
    beginning_time: string;
    ending_time: string;
    room: string;
    school_name: string;
    substitute_name: string | null;
    teacher_name:string
  }[];
  status: 'accepted' | 'pending' | 'searching' | 'revoked';
}


export interface SchoolJob {
  teacher_name: string
  date: string,
  beginning_time : string,
  ending_time: string,
  grade: string,
  subject: string,
  status: string,
  classCount: number,
  substitute_name: string | null
}

export function schoolContentFetcher(assignmentList:SchoolAssignment[]): SchoolJob[]{
  return assignmentList
  .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()).
  map(assignment =>{
    const teacher_name = [...new Set(assignment.classes.map(cls => cls.teacher_name))].join(", ");
    const grades = [...new Set(assignment.classes.map(c=> c.grade))].join(",")
    const subjects = [...new Set(assignment.classes.map(c=> c.subject))].join(",")
    const substitute_name = assignment.classes[0].substitute_name;
    const displaySubstitute = substitute_name && substitute_name.trim() !== "" 
      ? substitute_name 
      : "No substitute yet";
    const dateObj = new Date(assignment.date);
    const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' }); // Gets "Monday", "Tuesday", etc.
    const formattedDate = dateObj.toLocaleDateString('fi-FI'); // Gets "DD.MM.YYYY"
    const date = `${formattedDate} ${dayOfWeek}`;
    const status = assignment.status.charAt(0).toUpperCase() + assignment.status.slice(1)
    const beginning_time = assignment.classes[0].beginning_time.slice(11,16)
    const ending_time= assignment.classes[assignment.classes.length-1].ending_time.slice(11,16)
    return{
      teacher_name:teacher_name,
      date:date,
      beginning_time:beginning_time,
      ending_time:ending_time,
      grade: grades,
      subject: subjects,
      status:status,
      classCount: assignment.classes.length,
      substitute_name: displaySubstitute
      
    }

  })
}

const SchoolUpcomings = () => {
    const [jobs,setJobs] = useState<SchoolJob[]>([]);
    const [assignments, setAssignments] = useState<SchoolAssignment[]>([]); // Add assignments state
    const [selectedAssignment, setSelectedAssignment] = useState<SchoolAssignment | null>(null); // Add modal state
    const [modalOpen, setModalOpen] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(()=>{
        const fetchAssignments = async () => {
            try {
                const teacherID = getUserID();
                if (!teacherID) {
                    setError('No school ID found');
                    return;
                }
                const teacherInfo = await get_teacher_info(teacherID) as TeacherData;
                if (!teacherInfo) {
                    setError('Failed to fetch teacher info');
                    return;
                }

                const schoolID = teacherInfo.school_ID;
                if (!schoolID) {
                    setError('No school ID found for teacher');
                    return;
                }
                const response = await get_all_assignments_of_school(schoolID);

                if(response && response.success){
                    setAssignments(response.assignments);
                    const processedJobs = schoolContentFetcher(response.assignments)
                    setJobs(processedJobs)
                }else {
                    setError('Failed to fetch assignments');
                }
            }catch(error){
                setError("Error")
            }finally {
                setLoading(false);
            }
        }
        fetchAssignments()
    },[])

    const handleCardClick = (job: SchoolJob) => {
        const match = assignments.find((assignment) => {
          const dateObj = new Date(assignment.date);
          const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
          const formattedDate = dateObj.toLocaleDateString('fi-FI');
          const composed = `${formattedDate} ${dayOfWeek}`;
          const start = assignment.classes[0].beginning_time.slice(11, 16);
          return composed === job.date && start === job.beginning_time;
        });
    
        if (match) {
          setSelectedAssignment(match);
          setModalOpen(true);
        }
    };

    // Add modal close handler
    const handleCloseModal = () => {
        setModalOpen(false);
        setSelectedAssignment(null);
    };
    if (loading) {
        return <div>Loading assignments...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }
    return (
        <div className={styles.galleryWrapper}>
          <div className={styles.cardRail}>
            <div className={styles.cardContainer}>
              {jobs.map((job, index) => (
                <div key={`${job.date}-${job.beginning_time}-${index}`} className={styles.cardWrapper}>
                  <SchoolJobsCard job={job} onClick={() => handleCardClick(job)} />
                </div>
              ))}
            </div>
          </div>
    
          <SchoolAssignmentDetailsModal
            open={modalOpen}
            onClose={handleCloseModal}
            assignment={selectedAssignment}
          />
        </div>
      );
    };
    

export default SchoolUpcomings;
