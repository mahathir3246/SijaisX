
import {
  Avatar,
  Panel,
  Button,
  Loader,
  Input,
  toaster,
  Message
} from 'rsuite';
import subStyles from '../../../scss_stylings/substitute.module.scss';
import { getUserID } from '../../../functions/auth';
import { get_substitute_info , update_substitute_profile} from '../../../functions/api_calls';
import { useEffect, useState } from 'react';

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
    if(substitute){
      setName(substitute.name);
      setEmail(substitute.email);
      setPhone(substitute.phone_number);
    }
  }

  const handleCancel = () =>{
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
    <Panel 
    bordered
    className={subStyles.profileContainer}>
            <div className={subStyles.upperHalfContainer}>
                <div className={subStyles.profile}>Profile</div>
                  <Avatar circle size='xxl' ></Avatar>¨
                  {isEditing ? (
                    <>
                    <div>
                      <label>Name:</label>
                      <Input 
                      className={subStyles.name}
                      value={name}
                      onChange={setName}
                      placeholder='Enter your name'
                      />
                    </div>
                    <div>
                      <label>phone:</label>
                      <Input 
                      className={subStyles.email}
                      value={phone}
                      onChange={setPhone}
                      placeholder='Enter your phone number'
                      />
                    </div>
                    <div>
                    <label>email:</label>
                    <Input 
                    className={subStyles.phone_number}
                    value={email}
                    onChange={setEmail}
                    placeholder='Enter your email'
                    />
                    </div>
                    </>
                    
                    
                  ): 
                  <>
                  <h3 className={subStyles.name}>{substitute.name || 'Unknown Teacher'}</h3>
                  <p className={subStyles.email}>{substitute.email || 'No email'}</p>
                  <p className={subStyles.phone}>{substitute.phone_number || 'No phone'}</p>
                  </>
                  }

                </div>

            <div>
              {isEditing ? (
                <>
                <Button appearance="primary" block className= {subStyles.editProfileButton} onClick={handleSave} loading = {isSaving}>
                  Save
                </Button>
                <Button appearance="primary" block className= {subStyles.editProfileButton} onClick={handleCancel}>
                  Cancel
                </Button>
                </>
              ):
                <Button appearance="primary" block className= {subStyles.editProfileButton} onClick={handleEdit}>
                  Edit Profile
                </Button>
              }
            </div>
    </Panel>
  );
};

export default SubstituteProfile;
