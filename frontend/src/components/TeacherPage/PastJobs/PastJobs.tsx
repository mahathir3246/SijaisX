import { useEffect, useState } from 'react';
import TeacherSidebar from '../layout/TeacherSidebar';
import Logo from '../../../Logo/Logo';
import { Header, Button, Table, Badge, Panel, Content } from 'rsuite';
import "../TeacherDashboard.scss"
import PostAJobPopup from '../JobPosting/PostAJobPopup';
import { get_completed_batches_for_teacher } from '../../../functions/api_calls';
import { getUserID } from '../../../functions/auth';


const { Column, HeaderCell, Cell } = Table;


export interface ClassBE {
    subject:string,
    grade:string,
    beginning_time:string,
    ending_time:string,
    duration:number,
    room:string,
    notes:string
}
export interface BatchBE {
    date:string,
    school_name:string,
    teacher_name:string,
    teacher_email:string,
    batch_ID:string,
    classes:ClassBE[]
}

export interface PastJobsBE {
    batches:BatchBE[]
}

export interface PastJobsFE {
    date:string,
    beginning_time:string,
    ending_time:string,
    lessons:number,
    classes:string,
    subject:string,

}

export const mapPastJobs = (batch: BatchBE[]): PastJobsFE[] => {
    return batch
    .sort((a,b) => new Date(a.date).getTime() - new Date(b.date).getTime())
    .map((job)=>{
      const dateObj = new Date(job.date)
      const dayOfWeek = dateObj.toLocaleDateString("en-US", {weekday: "long"});
      const formattedDate= dateObj.toLocaleDateString("fi-FI");
      const date= `${formattedDate} ${dayOfWeek}`;
      const beginning_time= job.classes[0].beginning_time.slice(11,16);
      const ending_time = job.classes[job.classes.length-1].ending_time.slice(11,16);
      const lessons = job.classes.length
      const classes = [...new Set(job.classes.map((cls) => cls.grade))].join(",");
      const subject = [...new Set(job.classes.map((cls) => cls.subject))].join(",");

      return{
        date: date,
        beginning_time:beginning_time,
        ending_time:ending_time,
        lessons:lessons,
        classes:classes,
        subject:subject
      }
      
    })
}


const PastJobs = () => {
  const [activeKey, setActiveKey] = useState('past-jobs');
  const [collapsed, setCollapsed] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [postJobModalOpen, setPostJobModalOpen] = useState(false);

  const [pastJobs, setPastJobs] = useState<PastJobsFE[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const teacherID = getUserID();
    if (!teacherID) {
      setError('No teacher ID found, please log in again.');
      setLoading(false);
      return;
    }
  
    const fetchPastJobs = async () => {
      try {
        setLoading(true);
        setError(null);
  
        const batches = await get_completed_batches_for_teacher(
          teacherID,
          new Date().toISOString()
        );
  
        if (!batches || batches.length === 0) {
          setPastJobs([]);
          return;
        }
  
        setPastJobs(mapPastJobs(batches));
      } catch (err) {
        console.error('Failed to fetch past jobs:', err);
        setError('Something went wrong while loading past jobs.');
        setPastJobs([]);
      } finally {
        setLoading(false);
      }
    };
  
    fetchPastJobs();
  }, []);

  const handleSidebarSelect = (key: string) => {
    if (key === 'post-job') {
      setPostJobModalOpen(true);
      return;
    }
    setActiveKey(key);
  };
  return (
    <div className={`dashboard-container ${collapsed ? 'sidebar-collapsed' : ''}`}>
      <TeacherSidebar
        activeKey={activeKey}
        onSelect={handleSidebarSelect}
        collapsed={collapsed}
        onToggle={() => setCollapsed((prev) => !prev)}
        onPostJobClick={() => setPostJobModalOpen(true)}
      />
      <div className="dashboard-main">
        <Header className="dashboard-header">
          <Logo size="small" showText={false} />
          <div className="header-right">
            <span className="page-title">My Jobs</span>
          </div>
        </Header>

        <Content className="dashboard-content">
          <div className="section-header">
            <h3>Your Past Job Postings</h3>
            <p>Manage and track your previous job postings</p>
          </div>

          <div className="school-jobs-section">
            <h3>All past job postings</h3>
            <p className="section-subtitle">
              Click ‘View Details’ to see more info about the job, assigned substitute, and class details.
            </p>

            <Panel bordered>
            <Table
                bordered
                data={pastJobs}
                autoHeight
                style={{ marginTop: 20, minHeight: 280 }}
              >
                <Column flexGrow={2}>
                  <HeaderCell>Date</HeaderCell>
                  <Cell dataKey="date" />
                </Column>

                <Column flexGrow={1}>
                  <HeaderCell>From</HeaderCell>
                  <Cell dataKey="beginning_time" />
                </Column>

                <Column flexGrow={1}>
                  <HeaderCell>To</HeaderCell>
                  <Cell dataKey="ending_time" />
                </Column>

                <Column flexGrow={1}>
                  <HeaderCell>Lessons</HeaderCell>
                  <Cell dataKey="lessons" />
                </Column>

                <Column flexGrow={2}>
                  <HeaderCell>Class</HeaderCell>
                  <Cell dataKey="classes" />
                </Column>

                <Column flexGrow={3}>
                  <HeaderCell>Subject</HeaderCell>
                  <Cell dataKey="subject" />
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
      <PostAJobPopup open={postJobModalOpen} onClose={() => setPostJobModalOpen(false)} />
    </div>
  );
};

export default PastJobs	;