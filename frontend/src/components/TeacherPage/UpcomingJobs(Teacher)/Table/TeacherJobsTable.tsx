import { useState } from 'react';
import TeacherSidebar from '../../layout/TeacherSidebar';
import Logo from '../../../../Logo/Logo';
import { Header, Button, Table, Badge, Panel, Content } from 'rsuite';
import "../../TeacherDashboard.scss"
import AssignmentDetailsModal from '../Details';
import { useTeacherJobs, getStatusColor, matchJobToAssignment, Job } from '../TeacherJobsHook';
import PostAJobPopup from '../../JobPosting/PostAJobPopup';
const { Column, HeaderCell, Cell } = Table;

const TeacherUpcomingsTable = () => {
  const { assignments, jobs, loading, error } = useTeacherJobs();
  const [activeKey, setActiveKey] = useState('my-jobs');
  const [collapsed, setCollapsed] = useState(true);
  const [selectedAssignment, setSelectedAssignment] = useState<typeof assignments[number] | null>(null);
  const [modalOpen, setModalOpen] = useState(false);
  const [postJobModalOpen, setPostJobModalOpen] = useState(false);

  const handleSidebarSelect = (key: string) => {
    if (key === 'post-job') {
      setPostJobModalOpen(true);
      return;
    }
    setActiveKey(key);
  };

  const handleRowClick = (job: Job) => {
    const match = matchJobToAssignment(assignments, job);
    if (match) {
      setSelectedAssignment(match);
      setModalOpen(true);
    }
  };

  const handleCloseModal = () => {
    setModalOpen(false);
    setSelectedAssignment(null);
  };

  if (loading) return <div>Loading assignments...</div>;
  if (error) return <div>Error: {error}</div>;

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
            <h3>Your Substitute Requests</h3>
            <p>Manage and track your job postings</p>
          </div>

          <div className="school-jobs-section">
            <h3>All upcoming job postings</h3>
            <p className="section-subtitle">
              Click ‘View Details’ to see class notes, applicants, or edit the assignment.
            </p>

            <Panel bordered>
              <Table
                bordered
                onRowClick={handleRowClick}
                data={jobs}
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
                  <Cell dataKey="classCount" />
                </Column>

                <Column flexGrow={2}>
                  <HeaderCell>Class</HeaderCell>
                  <Cell dataKey="grade" />
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
                    {(rowData: Job) => (
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
      <PostAJobPopup open={postJobModalOpen} onClose={() => setPostJobModalOpen(false)} />
    </div>
  );
};

export default TeacherUpcomingsTable;