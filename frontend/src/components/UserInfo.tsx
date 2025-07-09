import { Button, Panel, Avatar, Divider } from 'rsuite';
import { getCurrentUser, logout } from '../functions/auth';
import ExitIcon from '@rsuite/icons/Exit';

const UserInfo = () => {
  const user = getCurrentUser();

  if (!user) {
    return null;
  }

  const handleLogout = () => {
    if (window.confirm('Are you sure you want to logout?')) {
      logout();
    }
  };

  return (
    <Panel 
      bordered 
      shaded 
      style={{ 
        maxWidth: '300px', 
        margin: '20px auto',
        textAlign: 'center'
      }}
    >
      <Avatar 
        circle 
        size="lg" 
        style={{ 
          backgroundColor: user.role === 'teacher' ? '#3498db' : '#e74c3c',
          marginBottom: '10px'
        }}
      >
        {user.email.charAt(0).toUpperCase()}
      </Avatar>
      
      <h5>{user.email}</h5>
      <p style={{ color: '#888', textTransform: 'capitalize' }}>
        {user.role}
      </p>
      <p style={{ color: '#aaa', fontSize: '12px' }}>
        ID: {user.user_ID}
      </p>
      
      <Divider />
      
      <Button 
        appearance="ghost" 
        color="red" 
        startIcon={<ExitIcon />}
        onClick={handleLogout}
        block
      >
        Logout
      </Button>
    </Panel>
  );
};

export default UserInfo;