import { useEffect, useState } from 'react';
import { get_all_assignments_of_teacher } from '../../../../functions/api_calls';
import { getUserID } from '../../../../functions/auth';
import TeacherSidebar from '../../TeacherSidebar';
import Logo from '../../../../Logo/Logo';
import { Header, Button, Table, Badge, Panel, Content } from 'rsuite';
import "../../TeacherDashboard.scss";
import AssignmentDetailsModal from '../Cards/CardPopup';


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
  classCount: number,
  substitute_name: string
}


export function cardContentfetcher(assignmentList:Assignment[]): Job[]{
  return assignmentList
  .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()).
  map(assignment =>{
    const grades = [...new Set(assignment.classes.map(c=> c.grade))].join(",")
    const subjects = [...new Set(assignment.classes.map(c=> c.subject))].join(",")
    const dateObj = new Date(assignment.date);
    const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' }); // Gets "Monday", "Tuesday", etc.
    const formattedDate = dateObj.toLocaleDateString('fi-FI'); // Gets "DD.MM.YYYY"
    const date = `${formattedDate} ${dayOfWeek}`;
    const status = assignment.status.charAt(0).toUpperCase() + assignment.status.slice(1)
    const beginning_time = assignment.classes[0].beginning_time.slice(11,16)
    const ending_time= assignment.classes[assignment.classes.length-1].ending_time.slice(11,16)
    const substitute =
       assignment.classes[0]?.substitute_name?.trim() || '-';
    return{
      date:date,
      beginning_time:beginning_time,
      ending_time:ending_time,
      grade: grades,
      subject: subjects,
      status:status,
      classCount: assignment.classes.length,
      substitute_name: substitute
    }

  })
}

const statusToken: Record<string, string> = {
    searching: 'searching',
    pending: 'pending',
    accepted: 'accepted',
    revoked: 'revoked',
  };
  
export const getStatusColor = (status: string) =>
    statusToken[status.toLowerCase()] ?? 'pending';

const TeacherUpcomingsTable = () => {

    const [activeKey, setActiveKey] = useState('my-jobs');
    const [collapsed, setCollapsed] = useState(false);


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
                <span className="page-title">My jobs</span>
            </div>
            </Header>

            <Content className="dashboard-content">
                <div className="section-header">
                    <h3>Your Substitute Requests</h3>
                    <p>Manage and track your job postings</p>
                </div>
                <div className="school-jobs-section">
                    <h3>All upcoming job postings</h3>
                    <p className="section-subtitle">Click ‘View Details’ to see class notes, applicants, or edit the assignment.</p>

                    <Panel bordered>
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
                                <HeaderCell>Lessons</HeaderCell>
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

                            <Column flexGrow={2}>
                                <HeaderCell>Substitute</HeaderCell>
                                <Cell dataKey="substitute_name" />
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
        <AssignmentDetailsModal
            open={modalOpen}
            onClose={handleCloseModal}
            assignment={selectedAssignment}
        />
    </div>
    )
};

export default TeacherUpcomingsTable;