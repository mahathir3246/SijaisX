
import { useState, useEffect } from 'react';
import {
  Avatar,
  Panel,
  Grid,
  Row,
  Col,
  Button,
  Loader
} from 'rsuite';
import teacherStyles from '../../../scss_stylings/teacher.module.scss';
import { getUserID } from '../../../functions/auth';
import { get_teacher_info } from '../../../functions/api_calls';

const TeacherProfile = () => {
  const [teacher, setTeacher] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeacherData = async () => {
      try {
        const teacherID = getUserID(); // Get logged-in teacher's ID
        
        if (!teacherID) {
          setError('No teacher ID found');
          setLoading(false);
          return;
        }

        const teacherData = await get_teacher_info(teacherID);
        
        if (teacherData) {
          setTeacher(teacherData);
        } else {
          setError('Failed to load teacher data');
        }
      } catch (err) {
        console.error('Error fetching teacher data:', err);
        setError('Error loading profile');
      } finally {
        setLoading(false);
      }
    };

    fetchTeacherData();
  }, []);

  if (loading) {
    return (
      <Panel bordered className={teacherStyles.profileContainer}>
        <div style={{ textAlign: 'center', padding: '40px' }}>
          <Loader size="lg" content="Loading profile..." />
        </div>
      </Panel>
    );
  }

  if (error) {
    return (
      <Panel bordered className={teacherStyles.profileContainer}>
        <div style={{ textAlign: 'center', padding: '40px' }}>
          <p style={{ color: 'red' }}>Error: {error}</p>
        </div>
      </Panel>
    );
  }

  if (!teacher) {
    return (
      <Panel bordered className={teacherStyles.profileContainer}>
        <div style={{ textAlign: 'center', padding: '40px' }}>
          <p>No teacher data available</p>
        </div>
      </Panel>
    );
  }

  return (
    <Panel 
      bordered
      className={teacherStyles.profileContainer}>
      <div className={teacherStyles.upperHalfContainer}>
        <div className={teacherStyles.profile}>Profile</div>
        <Avatar circle size='xxl'>
          {teacher.name ? teacher.name.charAt(0).toUpperCase() : 'T'}
        </Avatar>
        <h3 className={teacherStyles.name}>{teacher.name || 'Unknown Teacher'}</h3>
        <p className={teacherStyles.email}>{teacher.email || 'No email'}</p>
        <p className={teacherStyles.phone}>{teacher.phone_number || 'No phone'}</p>
      </div>

      <div>
        <Grid fluid>
          {[
            ['Teacher ID', teacher.teacher_ID || 'N/A'],
            ['School ID', teacher.school_ID || 'N/A'],
            ['Email', teacher.email || 'N/A'],
            ['Phone', teacher.phone_number || 'N/A']
          ].map(([label, value], index) => (
            <Row key={index} className={teacherStyles.meta_row}>
              <Col xs={7} className={teacherStyles.label}>
                {label}:
              </Col>
              <Col xs={17} className={teacherStyles.value}>
                {value}
              </Col>
            </Row>
          ))}
        </Grid>
        <Button appearance="primary" block className={teacherStyles.editProfileButton}>
          Edit Profile
        </Button>
      </div>
    </Panel>
  );
};

export default TeacherProfile;
