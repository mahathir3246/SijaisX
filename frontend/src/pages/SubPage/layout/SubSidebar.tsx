import { Sidebar, Nav, Button } from 'rsuite';
import { FiHome, FiUser, FiBriefcase, FiClock, FiMessageSquare, FiMenu } from 'react-icons/fi';
import "../../TeacherPage/TeacherDashboard.scss"

const navItems = [
  { eventKey: 'dashboard', label: 'My Dashboard', icon: <FiHome />, href: '/substitute/dashboard' },
  { eventKey: 'profile', label: 'My Profile', icon: <FiUser />, href: '/substitute/profile' },
  { eventKey: 'available-jobs', label: 'My Available Jobs', icon: <FiBriefcase />, href: '/substitute/available-jobs' },
  { eventKey: 'applied-jobs', label: 'My Applied Jobs', icon: <FiBriefcase />, href: '/substitute/applied-jobs' },
  { eventKey: 'accepted-jobs', label: 'My Accepted Jobs', icon: <FiBriefcase />, href: '/substitute/accepted-jobs' },
  { eventKey: 'history', label: 'Past Jobs', icon: <FiClock />, href: '/substitute/history' },
  { eventKey: 'messages', label: 'Messages', icon: <FiMessageSquare />, href: '/substitute/messages' },
];

type SubSidebarProps = {
  activeKey: string;
  onSelect: (key: string) => void;
  collapsed: boolean;
  onToggle: () => void;
};

export default function SubSidebar({
  activeKey,
  onSelect,
  collapsed,
  onToggle,
}: SubSidebarProps) {
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
          <Nav.Item
            key={item.eventKey}
            eventKey={item.eventKey}
            icon={item.icon}
            href={item.eventKey === 'post-job' ? undefined : item.href}
            onClick={
              item.eventKey === 'post-job'
                ? (event) => {
                    event.preventDefault();
                    onSelect(item.eventKey);
                  }
                : undefined
            }
          >
            {!collapsed && item.label}
          </Nav.Item>
        ))}
      </Nav>
    </Sidebar>
  );
}