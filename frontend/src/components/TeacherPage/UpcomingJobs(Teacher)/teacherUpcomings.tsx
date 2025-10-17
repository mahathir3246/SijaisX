
import { Table } from 'rsuite';
import '../../../scss_stylings/card.module.scss'
import styles from "../../../scss_stylings/card.module.scss"
import AssignmentDetailsModal from './Cards/CardPopup';
import { useEffect, useState } from 'react';
import { get_all_assignments_of_teacher } from '../../../functions/api_calls';
import { getUserID } from '../../../functions/auth';
import ClassCard from './Cards/ClassCard';


const { Column, HeaderCell, Cell } = Table;

export interface Assignment {
  date: string;
  batch_ID?: string;
  classes: {
    assignment_ID: string;
    subject: string;
    grade: string;
    notes?: string;
    beginning_time: string;
    ending_time: string;
    room: string;
    school_name: string;
    substitute_name: string | null;
  }[];
  status: 'accepted' | 'pending' | 'searching' | 'revoked';
}

export interface Job {
  date: string,
  beginning_time : string,
  ending_time: string,
  grade: string,
  subject: string,
  status: string,
  classCount: number
}


export function cardContentfetcher(assignmentList:Assignment[]): Job[]{
  return assignmentList.map(assignment =>{
    const grades = [...new Set(assignment.classes.map(c=> c.grade))].join(",")
    const subjects = [...new Set(assignment.classes.map(c=> c.subject))].join(",")
    const dateObj = new Date(assignment.date);
    const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' }); // Gets "Monday", "Tuesday", etc.
    const formattedDate = dateObj.toLocaleDateString('fi-FI'); // Gets "DD.MM.YYYY"
    const date = `${formattedDate} ${dayOfWeek}`;
    const status = assignment.status.charAt(0).toUpperCase() + assignment.status.slice(1)
    const beginning_time = assignment.classes[0].beginning_time.slice(11,16)
    const ending_time= assignment.classes[assignment.classes.length-1].ending_time.slice(11,16)
    return{
      date:date,
      beginning_time:beginning_time,
      ending_time:ending_time,
      grade: grades,
      subject: subjects,
      status:status,
      classCount: assignment.classes.length
    }

  })
}


const TeacherUpcomings = () => {
    const [jobs,setJobs] = useState<Job[]>([]);
    const [assignments, setAssignments] = useState<Assignment[]>([]);
    const [selectedAssignment, setSelectedAssignment] = useState<Assignment | null>(null);
    const [modalOpen, setModalOpen] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(()=>{
        const fetchAssignments = async () => {
            try {
                const teacherID = getUserID();
                if (!teacherID) {
                    setError('No teacher ID found');
                    return;
                }

                const response = await get_all_assignments_of_teacher(teacherID);

                if(response && response.success){
                    setAssignments(response.assignments);
                    const processedJobs = cardContentfetcher(response.assignments)
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

    const handleCardClick = (job: Job) => {
        // Find the corresponding assignment from the original data
        const correspondingAssignment = assignments.find(assignment => {
            const dateObj = new Date(assignment.date);
            const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
            const formattedDate = dateObj.toLocaleDateString('fi-FI');
            const date = `${formattedDate} ${dayOfWeek}`;
            const beginning_time = assignment.classes[0].beginning_time.slice(11,16);
            
            return date === job.date && beginning_time === job.beginning_time;
        });

        if (correspondingAssignment) {
            setSelectedAssignment(correspondingAssignment);
            setModalOpen(true);
        }
    };

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
    return(
        <div>
            <div className={`${styles.galleryWrapper} ${styles.cardRail}`}>  
                <div className={styles.cardContainer}>
                {jobs.map((job, index) => {
                    const correspondingAssignment = assignments.find(assignment => {
                        const dateObj = new Date(assignment.date);
                        const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' });
                        const formattedDate = dateObj.toLocaleDateString('fi-FI');
                        const date = `${formattedDate} ${dayOfWeek}`;
                        const beginning_time = assignment.classes[0].beginning_time.slice(11,16);
                        return date === job.date && beginning_time === job.beginning_time;
                    });
                    const assignmentIds = correspondingAssignment?.classes.map(c => c.assignment_ID) || [];
                    
                    return (
                        <div key={`${job.date}-${job.beginning_time}-${job.subject}-${index}`}>
                            <ClassCard 
                                job={job} 
                                onClick={() => handleCardClick(job)}
                                assignmentIds={assignmentIds}
                            />
                        </div>
                    );
                })}
                </div>

                <AssignmentDetailsModal 
                    open={modalOpen} 
                    onClose={handleCloseModal} 
                    assignment={selectedAssignment} 
                />
            </div>
            <Table 
              bordered 
              onRowClick={(rowData) => handleCardClick(rowData)}
              data={jobs}
              autoHeight
              style={{ marginTop: 20,
                    minHeight: 280 }}>


                <Column flexGrow={2}>
                    <HeaderCell>Date</HeaderCell>
                    <Cell dataKey='date'/>
                </Column>

                <Column flexGrow={1}>
                    <HeaderCell>From</HeaderCell>
                    <Cell dataKey='beginning_time'/>
                </Column>

                <Column flexGrow={1}>
                    <HeaderCell>To</HeaderCell>
                    <Cell dataKey='ending_time'/>
                </Column>
                
                <Column flexGrow={1}>
                    <HeaderCell>Amount</HeaderCell>
                    <Cell dataKey='classCount'/>
                </Column>

                <Column flexGrow={2}>
                    <HeaderCell>Class</HeaderCell>
                    <Cell dataKey="grade"/>               
                </Column>

                <Column flexGrow={3}>
                    <HeaderCell>Subject</HeaderCell>
                    <Cell dataKey="subject" />
                </Column>

                <Column flexGrow={1}>
                    <HeaderCell>Status</HeaderCell>
                    <Cell dataKey='status'/>
                </Column>

            </Table>
        </div>
    )
};

export default TeacherUpcomings;
