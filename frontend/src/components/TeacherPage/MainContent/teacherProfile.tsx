
import {
  Avatar,
  Panel,
  Button,
  Loader
} from 'rsuite';
import teacherStyles from '../../../scss_stylings/teacher.module.scss';
import { getUserID } from '../../../functions/auth';
import { get_teacher_info, get_school_info } from '../../../functions/api_calls';
import { useEffect, useState } from 'react';

const TeacherProfile = () => {

  interface SchoolData{
    school_ID: string,
    school_name: string
  }

  interface TeacherData{
    teacher_ID: string,
    name: string,
    phone_number: string,
    email: string,
    password: string,
    school_ID: string
  }
  const [teacher, setTeacher] = useState<TeacherData | null>(null);
  const [school, setSchool] = useState<SchoolData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getTeacherData = async () =>{
      try{
        const teacherID = getUserID();

        if(!teacherID || teacherID === "") {
          setError('No teacher ID found');
          setLoading(false);
          return;
        }

        const teacherInfo = await get_teacher_info(teacherID);

        if(teacherInfo){
          setTeacher(teacherInfo as TeacherData)

          const schoolInfo = await get_school_info((teacherInfo as TeacherData).school_ID);
          if (schoolInfo) {
            setSchool(schoolInfo as SchoolData);
          }
        } else{
          setError("Error Loading profile")
        } 

      }catch(err){
        setError('Error loading profile')
        console.error('Error fetching teacher data:', err)
      } finally{
        setLoading(false)
      }
    }
    getTeacherData()
  } , []); 

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
                <Avatar circle size='xxl' ></Avatar>
                  <h3 className={teacherStyles.name}>{teacher.name || 'Unknown Teacher'}</h3>
                  <p className={teacherStyles.email}>{teacher.email || 'No email'}</p>
                  <p className={teacherStyles.phone}>{teacher.phone_number || 'No phone'}</p>
                  <p className={teacherStyles.school}>
                    {school ? school.school_name : 'Loading school...'}
                  </p>

            </div>

            <div>
              <Button appearance="primary" block className= {teacherStyles.editProfileButton}>
                Edit Profile
              </Button>
            </div>
    </Panel>
  );
};

export default TeacherProfile;
