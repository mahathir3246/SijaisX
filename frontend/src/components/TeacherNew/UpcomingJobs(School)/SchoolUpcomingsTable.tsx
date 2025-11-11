
import { Header, Button, Table, Badge, Panel, Content } from 'rsuite';
import '../../../scss_stylings/teacher.module.scss';
import { useState , useEffect} from 'react';
import SchoolAssignmentDetailsModal from './SchoolCardPopup';
import { getUserID } from '../../../functions/auth';
import { get_all_assignments_of_school, get_teacher_info } from '../../../functions/api_calls';
import { TeacherData } from '../TeacherProfile/TeacherProfile';
const { Column, HeaderCell, Cell } = Table;
import TeacherSidebar from '../TeacherSidebar';
import Logo from '../../../Logo/Logo';
import "../TeacherDashboard.scss";
import { getStatusColor } from '../UpcomingJobs(Teacher)/Table/TeacherUpcomings(table)';

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

const SchoolUpcomingsTable = () => {
    const [activeKey, setActiveKey] = useState('school-jobs');
    const [collapsed, setCollapsed] = useState(false);


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
        <div className={`dashboard-container ${collapsed ? 'sidebar-collapsed' : ''}`}>
            <TeacherSidebar
                activeKey={activeKey}
                onSelect={setActiveKey}
                collapsed={collapsed}
                onToggle={() => setCollapsed((prev) => !prev)}
            />
            <div className="dashboard-main">
                <Header className="dashboard-header">
                <Logo size="small" showText={false} />
                <div className="header-right">
                    <span className="page-title">School Jobs</span>
                </div>
                </Header>

                <Content className="dashboard-content">
                    <div className="section-header">
                        <h3>School-Wide Job Posts</h3>
                        <p>All substitute positions at your school</p>
                    </div>
                    <div className="school-jobs-section">
                        <h3>All School Jobs</h3>
                        <p className="section-subtitle">View all substitute job postings from your school</p>

                        <Panel bordered>
                            <Table 
                            bordered 
                            onRowClick={(rowData) => handleRowClick(rowData)}
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
                                    <HeaderCell>Lessons</HeaderCell>
                                    <Cell dataKey="classCount"/>               
                                </Column>


                                <Column flexGrow={2}>
                                    <HeaderCell>Teacher</HeaderCell>
                                    <Cell dataKey="teacher_name"/>               
                                </Column>

                                <Column flexGrow={2}>
                                    <HeaderCell>Substitute</HeaderCell>
                                    <Cell dataKey="substitute_name"/>               
                                </Column>


                                <Column flexGrow={2}>
                                    <HeaderCell>Class</HeaderCell>
                                    <Cell dataKey="grade"/>               
                                </Column>

                                <Column flexGrow={2}>
                                    <HeaderCell>Subject</HeaderCell>
                                    <Cell dataKey="subject" />
                                </Column>

                                <Column flexGrow={2} align="center">
                                    <HeaderCell>Status</HeaderCell>
                                        <Cell>
                                            {(rowData: any) => (
                                            <Badge
                                                content={rowData.status}
                                                style={{ backgroundColor: `var(--status-${getStatusColor(rowData.status)})` }}
                                            />
                                            )}
                                        </Cell>
                                </Column>

                                <Column width={150} align="center">
                                    <HeaderCell>Actions</HeaderCell>
                                    <Cell>
                                        <Button size="sm" appearance="primary">
                                            View Details
                                        </Button>
                                    </Cell>
                                </Column>

                            </Table>
                        </Panel>
                    </div>
                </Content>
            </div>
            <SchoolAssignmentDetailsModal 
                open={modalOpen} 
                onClose={handleCloseModal} 
                assignment={selectedAssignment} 
            />
        </div>
    )
};

export default SchoolUpcomingsTable;