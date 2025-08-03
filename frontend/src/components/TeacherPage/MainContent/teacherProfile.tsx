
import {
  Avatar,
  Panel,
  Button,
  Loader,
  Input,
  toaster,
  Message
} from 'rsuite';
import teacherStyles from '../../../scss_stylings/teacher.module.scss';
import { getUserID } from '../../../functions/auth';
import { get_teacher_info, get_school_info , update_teacher_profile} from '../../../functions/api_calls';
import { useEffect, useState } from 'react';


export interface TeacherData{
  teacher_ID: string,
  name: string,
  phone_number: string,
  email: string,
  password: string,
  school_ID: string
}


const TeacherProfile = () => {

  interface SchoolData{
    school_ID: string,
    school_name: string
  }

  const [teacher, setTeacher] = useState<TeacherData | null>(null);
  const [school, setSchool] = useState<SchoolData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  //edit profile usestates
  const[isEditing, setIsEditing] = useState(false);
  const[isSaving, setIsSaving] = useState(false);
  const[name, setName] = useState("");
  const[email, setEmail]= useState("");
  const [phone, setPhone] = useState("");

  const handleEdit = () =>{
    setIsEditing(true)
    if(teacher){
      setName(teacher.name);
      setEmail(teacher.email);
      setPhone(teacher.phone_number);
    }
  }

  const handleCancel = () =>{
    setIsEditing(false)
    if(teacher){
      setName(teacher.name);
      setPhone(teacher.phone_number);
      setEmail(teacher.email);
    }
  }

  const handleSave = async () => {
    if (!teacher) return;
    
    setIsSaving(true);
    
    try {
      const updatedData = {
        name: name.trim(),
        email: email.trim(),
        phone_number: phone.trim()
      };

      const result = await update_teacher_profile(teacher.teacher_ID, updatedData);
      
      if (result && result.success) {
        // Update local state with new data
        setTeacher(prev => prev ? {
          ...prev,
          name: updatedData.name,
          email: updatedData.email,
          phone_number: updatedData.phone_number
        } : null);
        
        setIsEditing(false);
        
        toaster.push(
          <Message type="success">
            Profile updated successfully!
          </Message>,
          { placement: 'topCenter', duration: 3000 }
        );
      } else {
        toaster.push(
          <Message type="error">
            Failed to update profile. Please try again.
          </Message>,
          { placement: 'topCenter', duration: 3000 }
        );
      }
    } catch (err) {
      console.error('Error updating profile:', err);
      toaster.push(
        <Message type="error">
          An error occurred while updating profile.
        </Message>,
        { placement: 'topCenter', duration: 3000 }
      );
    } finally {
      setIsSaving(false);
    }
  }

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
                  <Avatar circle size='xxl' ></Avatar>¨
                  {isEditing ? (
                    <>
                    <div>
                      <label>Name:</label>
                      <Input 
                      className={teacherStyles.name}
                      value={name}
                      onChange={setName}
                      placeholder='Enter your name'
                      />
                    </div>
                    <div>
                      <label>phone:</label>
                      <Input 
                      className={teacherStyles.email}
                      value={phone}
                      onChange={setPhone}
                      placeholder='Enter your phone number'
                      />
                    </div>
                    <div>
                    <label>email:</label>
                    <Input 
                    className={teacherStyles.phone_number}
                    value={email}
                    onChange={setEmail}
                    placeholder='Enter your email'
                    />
                    </div>
                    </>
                    
                    
                  ): 
                  <>
                  <h3 className={teacherStyles.name}>{teacher.name || 'Unknown Teacher'}</h3>
                  <p className={teacherStyles.email}>{teacher.email || 'No email'}</p>
                  <p className={teacherStyles.phone}>{teacher.phone_number || 'No phone'}</p>
                  <p className={teacherStyles.school}>
                    {school ? school.school_name : 'Loading school...'}
                  </p>
                  </>
                  }

                </div>

            <div>
              {isEditing ? (
                <>
                <Button appearance="primary" block className= {teacherStyles.editProfileButton} onClick={handleSave} loading = {isSaving}>
                  Save
                </Button>
                <Button appearance="primary" block className= {teacherStyles.editProfileButton} onClick={handleCancel}>
                  Cancel
                </Button>
                </>
              ):
                <Button appearance="primary" block className= {teacherStyles.editProfileButton} onClick={handleEdit}>
                  Edit Profile
                </Button>
              }
            </div>
    </Panel>
  );
};

export default TeacherProfile;
