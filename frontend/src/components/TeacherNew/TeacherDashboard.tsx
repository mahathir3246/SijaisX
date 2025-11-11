import { useState } from 'react';
import { Header, Content, Panel, Badge, Grid, Row, Col } from 'rsuite';
import Logo from '../../Logo/Logo';
import './TeacherDashboard.scss';
import TeacherUpcomings from './UpcomingJobs(Teacher)/Cards/TeacherUpcomings';
import SchoolUpcomings from './UpcomingJobs(School)/schoolupcomings';
import TeacherSidebar from './TeacherSidebar';

 const TeacherDashboard = () => {
    const [activeKey, setActiveKey] = useState('dashboard');
    const [collapsed, setCollapsed] = useState(false);
  
    const jobStats = {
      searching: 2,
      pending: 3,
      accepted: 5,
    };
  
    return (
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
              <span className="page-title">Teacher Dashboard</span>
            </div>
          </Header>
  
          <Content className="dashboard-content">
            <div className="welcome-section">
              <h3>Welcome! 👋</h3>
              <p>Manage your substitute requests and track ongoing jobs</p>
            </div>

            <Grid fluid>
              <Row gutter={16}>
                <Col xs={24} sm={8}>
                  <Panel bordered className="stat-card stat-card--searching">
                    <div className="stat-number">{jobStats.searching}</div>
                    <div className="stat-label">Searching for Subs</div>
                    <Badge className="stat-badge" content="Active" />
                  </Panel>
                </Col>
                <Col xs={24} sm={8}>
                  <Panel bordered className="stat-card stat-card--pending">
                    <div className="stat-number">{jobStats.pending}</div>
                    <div className="stat-label">Pending Approval</div>
                    <Badge className="stat-badge" content="Review" />
                  </Panel>
                </Col>
                <Col xs={24} sm={8}>
                  <Panel bordered className="stat-card stat-card--accepted">
                    <div className="stat-number">{jobStats.accepted}</div>
                    <div className="stat-label">Accepted Jobs</div>
                    <Badge className="stat-badge" content="Confirmed" />
                  </Panel>
                </Col>
              </Row>
            </Grid>
  
            <div className="section-header">
              <h3>My Job Posts</h3>
            </div>
  
            <TeacherUpcomings/>
  
            <div className="section-header">
              <h3>School Jobs Overview</h3>
              <p>All substitute requests from your school</p>
            </div>

            <SchoolUpcomings />
  
         </Content>
        </div>
      </div>
    );
  };
  
  export default TeacherDashboard;
