
import { Table } from 'rsuite';
import '../../../scss_stylings/teacher.module.scss';
import { useState , useEffect} from 'react';
import SchoolAssignmentDetailsModal from './SchoolCardPopup';
import { getUserID } from '../../../functions/auth';
import { get_all_assignments_of_school, get_teacher_info } from '../../../functions/api_calls';
import { TeacherData } from '../TeacherProfile/teacherProfile';
const { Column, HeaderCell, Cell } = Table;

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
  classCount: number
}

export function schoolContentFetcher(assignmentList:SchoolAssignment[]): SchoolJob[]{
  return assignmentList.map(assignment =>{
    const teacher_name = [...new Set(assignment.classes.map(cls => cls.teacher_name))].join(", ");
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
      teacher_name:teacher_name,
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

    const handleRowClick = (job: SchoolJob) => {
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
    return(
        <div>
            <Table 
              bordered data={jobs}
              autoHeight
              onRowClick={(rowData) => handleRowClick(rowData)}
              style={{ minHeight: 280 }}>

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
                    <Cell dataKey="classCount"/>               
                </Column>


                <Column flexGrow={2}>
                    <HeaderCell>Teacher</HeaderCell>
                    <Cell dataKey="teacher_name"/>               
                </Column>


                <Column flexGrow={2}>
                    <HeaderCell>Class</HeaderCell>
                    <Cell dataKey="grade"/>               
                </Column>

                <Column flexGrow={2}>
                    <HeaderCell>Subject</HeaderCell>
                    <Cell dataKey="subject" />
                </Column>

                <Column flexGrow={1}>
                    <HeaderCell>Status</HeaderCell>
                    <Cell dataKey='status'/>
                </Column>

            </Table>

            <SchoolAssignmentDetailsModal 
                open={modalOpen} 
                onClose={handleCloseModal} 
                assignment={selectedAssignment} 
            />
        </div>
    )
};

export default SchoolUpcomings;
