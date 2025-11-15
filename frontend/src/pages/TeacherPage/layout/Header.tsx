import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { FiBell, FiSettings, FiUser, FiLogOut, FiHelpCircle } from 'react-icons/fi';
import Logo from '../../../Logo/Logo';
import "../TeacherDashboard.scss"
import { Header } from 'rsuite';
import { logout , getUserID} from '../../../functions/auth';
import { get_teacher_info } from '../../../functions/api_calls';
import { getCurrentUser } from '../../../functions/auth';

interface HeaderProps{
    title:string;
}
const Navigation = ({title}:HeaderProps) => {

    const [showUserMenu, setShowUserMenu] = useState(false);
    const [userName, setUserName] = useState<string>('');
    const navigate = useNavigate();

    useEffect(() => {
      const fetchUserName = async () => {
          const teacherID = getUserID();
          if (teacherID) {
              try {
                  const teacherInfo = await get_teacher_info(teacherID);
                  if (teacherInfo && (teacherInfo as any).name) {
                      setUserName((teacherInfo as any).name);
                  }
              } catch (error) {
                  console.error('Error fetching teacher name:', error);
                  // Fallback to email if name fetch fails
                  const user = getCurrentUser();
                  if (user) {
                      setUserName(user.email);
                  }
              }
          }
      };
      fetchUserName();
  }, []);

  const handleProfileClick = () => {
      setShowUserMenu(false);
      navigate('/teacher/profile');
  };

  const handleLogoClick = () => {
    navigate('/teacher/dashboard');
  };

    return(
        <Header className="dashboard-header">
          <Logo size="small" showText={false} onClick={handleLogoClick} />
        <div className="header-center">
            <h3 className="header-title">{title}</h3>
        </div>

        <div className="header-right">
          <button className="header-icon-btn" title="Notifications">
            <FiBell />
            <span className="notification-badge">3</span>
          </button>
          <button className="header-icon-btn" title="Settings">
            <FiSettings />
          </button>
          <div className="user-menu-container">
            <button 
              className="header-user-btn" 
              title="Profile"
              onClick={() => setShowUserMenu(!showUserMenu)}
            >
              <FiUser />
              <span className="user-name">{userName}</span>
            </button>
            
            {showUserMenu && (
              <div className="user-dropdown-menu">
                <button className="menu-item" onClick={handleProfileClick} >
                  <FiUser />
                  <span>My Profile</span>
                </button>
                <button onClick={() => { setShowUserMenu(false); }} className="menu-item">
                  <FiHelpCircle />
                  <span>Help & Support</span>
                </button>
                <div className="menu-divider" />
                <button onClick={logout} 
              className="menu-item logout">
                  <FiLogOut />
                  <span>Sign Out</span>
                </button>
              </div>
            )}
          </div>
        </div>
        </Header>
    )
}

export default Navigation;