import { useState } from 'react';
import { Content, Panel, Badge, Grid, Row, Col, Button } from 'rsuite';
import "../TeacherDashboard.scss"
import TeacherCardGallery from '../UpcomingJobs(Teacher)/Cards/TeacherCardGalley';
import SchoolJobsCardGallery from '../UpcomingJobs(School)/Card/SchoolJobsCardGallery';
import TeacherSidebar from './TeacherSidebar';
import { FiPlusCircle } from 'react-icons/fi';
import PostAJobPopup from '../JobPosting/PostAJobPopup';
import Navigation from './Header';
import TeacherFooter from './Footer';

 const TeacherDashboard = () => {
    const [activeKey, setActiveKey] = useState('dashboard');
    const [collapsed, setCollapsed] = useState(true);
    const [postJobModalOpen, setPostJobModalOpen] = useState(false);
    const title = "My dashboard"

    const handleSidebarSelect = (key: string) => {
      if (key === 'post-job') {
        setPostJobModalOpen(true);
        return;
      }
      setActiveKey(key);
    };
  
    const jobStats = {
      searching: 2,
      pending: 3,
      accepted: 5,
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
          <Navigation title={title}/>
  
          <Content className="dashboard-content">
            <div className="welcome-section">
              <div>
              <h3>Welcome! 👋</h3>
              <p>Manage your substitute requests and track ongoing jobs</p>
              </div>
              <Button 
              appearance="primary" 
              size="lg"
              startIcon={<FiPlusCircle />}
              onClick={() => setPostJobModalOpen(true)}
              style={{ fontSize: '16px', fontWeight: 600 }}
            >
              Post a Job
            </Button>
            </div>
            

            <Grid fluid style={{marginBottom: "20px"}}>
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
  
            <TeacherCardGallery/>
  
            <div className="section-header">
              <h3>School Jobs Overview</h3>
              <p>All substitute requests from your school</p>
            </div>

            <SchoolJobsCardGallery />
  
         </Content>

        <TeacherFooter/>

        </div>
        <PostAJobPopup open={postJobModalOpen} onClose={() => setPostJobModalOpen(false)} />
      </div>
    );
  };
  
  export default TeacherDashboard;
