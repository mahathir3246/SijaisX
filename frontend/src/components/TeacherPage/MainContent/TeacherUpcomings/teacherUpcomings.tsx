
import { Table } from 'rsuite';
import '../../../../scss_stylings/card.module.scss';
import TeacherUpcomingsCardGallery from './Cards/TeacherUpcomingsCardGallery';
import { useEffect, useState } from 'react';
import { get_all_assignments_of_teacher } from '../../../../functions/api_calls';
import { getUserID } from '../../../../functions/auth';


const { Column, HeaderCell, Cell } = Table;

export interface Assignment {
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
  }[];
  status: 'accepted' | 'pending' | 'searching' | 'revoked';
}

export interface Job {
  date: string,
  beginning_time : string,
  ending_time: string,
  grade: string,
  subject: string,
  status: string
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
      status:status
    }

  })
}


const TeacherUpcomings = () => {
    const [jobs,setJobs] = useState<Job[]>([]);
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
                    const processedJobs = cardContentfetcher(response.assignments)
                    setJobs(processedJobs)
                }else {
                    setError('No assignments');
                }
            }catch(error){
                setError("Error")
            }finally {
                setLoading(false);
            }
        }
        fetchAssignments()
    },[])

    if (loading) {
    return <div>Loading assignments...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }
    return(
        <div>
            <TeacherUpcomingsCardGallery jobs={jobs}/>
            <Table 
              bordered 
              data={jobs}
              autoHeight
              style={{ marginTop: 20,     /* 10 px space above the table    */
                    minHeight: 280 }}  /* never shrink below 280 px      */>


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
