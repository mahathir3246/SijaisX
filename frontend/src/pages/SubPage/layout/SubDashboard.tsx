import { useState } from 'react';
import { Header, Content, Panel, Badge, Grid, Row, Col } from 'rsuite';
import Logo from '../../../Logo/Logo';
import "../../TeacherPage/TeacherDashboard.scss"
import SubSidebar from './SubSidebar';
import SubstituteJobsCard from '../jobs/components/Card/SubstituteJobsCard';
import { get_batch_of_available_assignments_for_substitute, get_batch_of_accepted_assignments_for_substitute, get_all_applied_batches_of_substitute } from '../../../functions/api_calls';
import Navigation from '../layout/Header';
import SubFooter from './Footer';


const title = "Substitute Dashboard";

 const SubDashboard = () => {
    const [activeKey, setActiveKey] = useState('dashboard');
    const [collapsed, setCollapsed] = useState(true);
    const jobStats = {
      searching: 2,
      pending: 3,
      accepted: 5,
    };
  
    return (
      <div className={`dashboard-container ${collapsed ? 'sidebar-collapsed' : ''}`}>
        <SubSidebar
            activeKey={activeKey}
            onSelect={setActiveKey}
            collapsed={collapsed}
            onToggle={() => setCollapsed((prev) => !prev)}
          />
        <div className="dashboard-main">
          <Navigation title={title} />
  
          <Content className="dashboard-content">
            <div className="welcome-section">
              <div>
              <h3>Welcome! 👋</h3>
              <p>Manage your substitute requests and track ongoing jobs</p>
              </div>
            </div>
            

          <Grid fluid style={{ marginBottom: '20px' }}>
            <Row gutter={16}>
              <Col xs={24} sm={8}>
                <Panel bordered className="stat-card stat-card--earnings">
                  <div className="stat-number">4</div>
                  <div className="stat-label">Jobs Completed</div>
                  <Badge className="stat-badge" content="Total" />
                </Panel>
              </Col>
              <Col xs={24} sm={8}>
                <Panel bordered className="stat-card stat-card--earnings">
                  <div className="stat-number">1478$</div>
                  <div className="stat-label">Earnings This Month</div>
                  <Badge className="stat-badge" content="Dec" />
                </Panel>
              </Col>
              <Col xs={24} sm={8}>
                <Panel bordered className="stat-card stat-card--pending">
                  <div className="stat-number">3</div>
                  <div className="stat-label">Pending Forms</div>
                  <Badge className="stat-badge" content="Action" />
                </Panel>
              </Col>
            </Row>
          </Grid>
  
            <div className="section-header">
              <h3>Available Jobs</h3>
              <p>All the jobs that are available to apply</p>
            </div>
            <SubstituteJobsCard
              apiFunction={get_batch_of_available_assignments_for_substitute}/>
  
  
            <div className="section-header">
              <h3>Applied Jobs</h3>
              <p>All the jobs you have applied to </p>
            </div>
            <SubstituteJobsCard
              apiFunction={get_all_applied_batches_of_substitute}/>

            <div className="section-header">
              <h3>Accepted Jobs</h3>
              <p>All the jobs you have been assigned to </p>
            </div>
            <SubstituteJobsCard
              apiFunction={get_batch_of_accepted_assignments_for_substitute}/>
  
         </Content>
         <SubFooter/>
        </div>
      </div>
    );
  };
  
  export default SubDashboard;
