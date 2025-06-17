
import {
  Avatar,
  Panel,
  Grid,
  Row,
  Col,
  Button
} from 'rsuite';
import teacherStyles from '../../../scss_stylings/teacher.module.scss';

const TeacherProfile = () => {
  // In real life you’d fetch this from context / API
  const teacher = {
    name: 'Riikka Ruusuvuori',
    email: 'riikka.ruusuvuori@eduvantaa.fi',
    phone: "+358402531030",
    school: 'Ruusuvuoren Koulu',
    department: 'Science',
    subjects: ['Biology', 'Chemistry'],
    yearsOfExperience: 7
  };

  return (
    <Panel 
    bordered
    className={teacherStyles.profileContainer}>
            <div className={teacherStyles.upperHalfContainer}>
                <div className={teacherStyles.profile}>Profile</div>
                <Avatar circle size='xxl' ></Avatar>
                <h3 className={teacherStyles.name}>{teacher.name}</h3>
                <p className={teacherStyles.email}>{teacher.email}</p>
                <p className={teacherStyles.phone}>{teacher.phone}</p>
            </div>

            <div>
                <Grid fluid>
                    {[
                    ['School', teacher.school],
                    ['Department', teacher.department],
                    ['Subjects', teacher.subjects.join(', ')],
                    ['Experience', `${teacher.yearsOfExperience} years`]
                    ].map(([label, value]) => (
                        <Row className={teacherStyles.meta_row}>
                            <Col xs={7} className={teacherStyles.label}>
                            {label}:
                            </Col>
                            <Col xs={17} className={teacherStyles.value}>
                            {value}
                            </Col>
                        </Row>
                    ))}
                </Grid>
              <Button appearance="primary" block className= {teacherStyles.editProfileButton}>
                Edit Profile
              </Button>
            </div>
    </Panel>
  );
};

export default TeacherProfile;
