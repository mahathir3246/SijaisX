import { Header, Loader,Content,toaster,Message, Button, Panel, Form, Input, Uploader } from 'rsuite';
import subStyles from '../../../scss_stylings/substitute.module.scss';
import { getUserID } from '../../../functions/auth';
import { get_substitute_info , update_substitute_profile, get_all_schools_of_substitute} from '../../../functions/api_calls';
import { useEffect, useState } from 'react';
import SubSidebar from '../layout/SubSidebar';
import "../../TeacherPage/TeacherDashboard.scss"
import Logo from '../../../Logo/Logo';

const SubstituteProfile = () => {


  interface SubstituteData{
    substitute_ID:string,
    name: string,
    phone_number: string,
    email:string,
    password:string,
    experience: number,
  }
  const [substitute, setSubstitute] = useState<SubstituteData | null>(null);
  const [schools, setSchools] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [activeKey, setActiveKey] = useState('profile');
  const [collapsed, setCollapsed] = useState(true);


  //edit profile usestates
  const[isEditing, setIsEditing] = useState(false);
  const[isSaving, setIsSaving] = useState(false);
  const[name, setName] = useState("");
  const[email, setEmail]= useState("");
  const [phone, setPhone] = useState("");

  const handleEdit = () =>{
    if (!substitute) return;
    setIsEditing(true)
    if(substitute){
      setName(substitute.name);
      setEmail(substitute.email);
      setPhone(substitute.phone_number);
    }
  }

  const handleCancel = () =>{
    if (!substitute) return;
    setIsEditing(false)
    if(substitute){
      setName(substitute.name);
      setPhone(substitute.phone_number);
      setEmail(substitute.email);
    }
  }

  const handleSave = async () => {
    if (!substitute) return;
    
    setIsSaving(true);
    
    try {
      const updatedData = {
        name: name.trim(),
        email: email.trim(),
        phone_number: phone.trim()
      };

      const result = await update_substitute_profile(substitute.substitute_ID, updatedData);
      
      if (result && result.success) {
        // Update local state with new data
        setSubstitute(prev => prev ? {
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
    const getSubstituteData = async () =>{
      try{
        const substitute_id = getUserID();

        if(!substitute_id || substitute_id === "") {
          setError('No substitute ID found');
          setLoading(false);
          return;
        }

        const subInfo = await get_substitute_info(substitute_id);

        if(subInfo){
          setSubstitute(subInfo as SubstituteData)
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
    getSubstituteData()
  } , []); 

  useEffect(() => {
  const getSchoolsData = async () => {
    try {
      const substitute_id = getUserID();
      
      if (!substitute_id || substitute_id === "") {
        return;
      }

      const schoolsResponse = await get_all_schools_of_substitute(substitute_id);
      
      if (schoolsResponse && schoolsResponse.success) {
        const schoolNames = schoolsResponse.schools?.map((school: any) => school.school_name) || [];
        setSchools(schoolNames);
      }
    } catch (err) {
      console.error('Error fetching schools:', err);
    }
  };
  
  getSchoolsData();
}, []);

  if (loading) {
  return (
    <Panel bordered className={subStyles.profileContainer}>
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <Loader size="lg" content="Loading profile..." />
      </div>
    </Panel>
  );
  }

  if (error) {
  return (
    <Panel bordered className={subStyles.profileContainer}>
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <p style={{ color: 'red' }}>Error: {error}</p>
      </div>
    </Panel>
  );
  }

  if (!substitute) {
  return (
    <Panel bordered className={subStyles.profileContainer}>
      <div style={{ textAlign: 'center', padding: '40px' }}>
        <p>No teacher data available</p>
      </div>
    </Panel>
  );
  }


  return (
    <div className={`dashboard-container ${collapsed ? 'sidebar-collapsed' : ''}`}>
        <SubSidebar
            activeKey={activeKey}
            onSelect={setActiveKey}
            collapsed={collapsed}
            onToggle={() => setCollapsed((prev) => !prev)}
          />
      <div className="dashboard-main">
        <Header className="dashboard-header">
          <Logo size="small" showText={false} />
          <div className="header-right">
            <span className="page-title">Teacher Profile</span>
          </div>
        </Header>

        <Content className="dashboard-content profile-content">
          <Panel bordered className="profile-panel">
            <h3>Personal Information</h3>
            <p className="section-subtitle">Update your personal details</p>

            <Form fluid>
              <div className="form-row">
              <Form.Group>
                <Form.ControlLabel>Name</Form.ControlLabel>
                <Input value={substitute.name} onChange={setName} disabled={!isEditing} />
              </Form.Group>
              </div>

              <Form.Group>
                <Form.ControlLabel>Email</Form.ControlLabel>
                <Input value={substitute.email} onChange={setEmail} disabled={!isEditing}/>
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Phone Number</Form.ControlLabel>
                <Input value={substitute.phone_number} onChange={setPhone} disabled={!isEditing} />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>School</Form.ControlLabel>
                <Input value={schools.join(', ')} disabled={true} />
              </Form.Group>

              {isEditing ? (
                <>
                  <Button appearance="primary" onClick={handleSave} loading={isSaving}>
                    Save Changes
                  </Button>
                  <Button appearance="subtle" onClick={handleCancel} disabled={isSaving}>
                    Cancel
                  </Button>
                </>
              ) : (
                <Button appearance="primary" onClick={handleEdit}>
                  Edit Profile
                </Button>
              )}
            </Form>
          </Panel>

          <Panel bordered className="profile-panel">
            <h3>Qualifications & Experience</h3>
            <p className="section-subtitle">Your teaching credentials and subjects</p>

            <Form fluid>
              <Form.Group>
                <Form.ControlLabel>Education</Form.ControlLabel>
                <Input defaultValue="Master of Education, University of Helsinki" />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Subjects</Form.ControlLabel>
                <Input defaultValue="Mathematics, Physics, Chemistry" />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Years of Experience</Form.ControlLabel>
                <Input type="number" defaultValue="5" />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Bio</Form.ControlLabel>
                <Input 
                  as="textarea" 
                  rows={4} 
                  defaultValue="Experienced substitute teacher with a passion for mathematics and sciences. Skilled in engaging students and adapting to different teaching environments."
                />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Upload CV</Form.ControlLabel>
                <Uploader action="//jsonplaceholder.typicode.com/posts/" draggable>
                  <div style={{ lineHeight: '100px' }}>Click or Drag files to this area to upload</div>
                </Uploader>
              </Form.Group>

              <Button appearance="primary">Update Qualifications</Button>
            </Form>
          </Panel>

          <Panel bordered className="profile-panel">
            <h3>Feedback & Ratings</h3>
            <p className="section-subtitle">Reviews from your previous assignments</p>

            <div className="rating-summary">
              <div className="rating-number">4.8 / 5.0</div>
              <div className="rating-meta">
                <span>Based on</span>
                <strong>24 reviews</strong>
              </div>
            </div>

            <div className="feedback-list">
              <Panel bordered className="feedback-item">
                <p className="feedback-school">From Jokiniemen Koulu</p>
                <p className="feedback-text">"Excellent teacher! Very professional and the students learned a lot."</p>
              </Panel>
              <Panel bordered className="feedback-item">
                <p className="feedback-school">From Simonkylän Koulu</p>
                <p className="feedback-text">"Great communication and preparation. Would definitely request again."</p>
              </Panel>
            </div>
          </Panel>
          </Content>
      </div>
    </div>

    
  );
    {/*}
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
    */}
};

export default SubstituteProfile;
