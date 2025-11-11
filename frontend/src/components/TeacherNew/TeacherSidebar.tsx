import { Sidebar, Nav, Button } from 'rsuite';
import { FiHome, FiUser, FiPlusCircle, FiBriefcase, FiClock, FiMessageSquare, FiMenu } from 'react-icons/fi';
import './TeacherDashboard.scss';

const navItems = [
  { eventKey: 'dashboard', label: 'My Dashboard', icon: <FiHome />, href: '/teacher/dashboard' },
  { eventKey: 'profile', label: 'My Profile', icon: <FiUser />, href: '/teacher/profile' },
  { eventKey: 'post-job', label: 'Post a Job', icon: <FiPlusCircle />, href: '/teacher/post-job' },
  { eventKey: 'my-jobs', label: 'My Job Posts', icon: <FiBriefcase />, href: '/teacher/my-jobs' },
  { eventKey: 'school-jobs', label: 'School Jobs', icon: <FiBriefcase />, href: '/teacher/school-jobs' },
  { eventKey: 'history', label: 'Past Jobs', icon: <FiClock />, href: '/teacher/history' },
  { eventKey: 'messages', label: 'Messages', icon: <FiMessageSquare />, href: '/teacher/messages' },
];

type TeacherSidebarProps = {
  activeKey: string;
  onSelect: (key: string) => void;
  collapsed: boolean;
  onToggle: () => void;
};

export default function TeacherSidebar({ activeKey, onSelect, collapsed, onToggle }: TeacherSidebarProps) {
  return (
    <Sidebar
      className={`dashboard-sidebar ${collapsed ? 'collapsed' : ''}`}
      width={collapsed ? 60 : 260}
      collapsible
    >
  <div className={`sidebar-header ${collapsed ? 'is-collapsed' : ''}`}>
    {!collapsed && <span className="sidebar-title">Menu</span>}
    <Button
      appearance="subtle"
      onClick={onToggle}
      className="collapse-btn"
      title={collapsed ? 'Expand menu' : 'Collapse menu'}
    >
      <FiMenu />
    </Button>
  </div>
      <Nav vertical activeKey={activeKey} onSelect={onSelect}>
        {navItems.map((item) => (
          <Nav.Item key={item.eventKey} eventKey={item.eventKey} icon={item.icon} href={item.href}>
            {!collapsed && item.label}
          </Nav.Item>
        ))}
      </Nav>
    </Sidebar>
  );
}