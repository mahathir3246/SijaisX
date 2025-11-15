import MenuIcon from '@rsuite/icons/Menu';
import { useState } from "react";
import { Button, Drawer } from "rsuite";
import ExitIcon from "@rsuite/icons/Exit";
import { Link } from 'react-router-dom';
import navigationStyles from "../../../scss_stylings/navbar.module.scss";

const NavDropdownMobile = () => {
  const [open, setOpen] = useState(false);
  const handleLinkEvent = () => setOpen(false);
  return (
    <div className={navigationStyles.dropdown}>
      <Button
        onClick={() => setOpen(true)}
        className={navigationStyles.menuButton}
        appearance="subtle"
      ><MenuIcon/>
      </Button>
      <Drawer
        placement="left"
        size="full"
        open={open}
        onClose={() => setOpen(false)}
      >
        <Drawer.Header
          className={navigationStyles.mobileDrawerHeaderSidebar}
          id="mobile-drawer-header-sidebar"
        >
          <div className={navigationStyles.logoContainer}>
            <div className={navigationStyles.logoSmall}>
              SijaisX
            </div>
          </div>
        </Drawer.Header>
        <Drawer.Body id="sidebar" className={navigationStyles.sidebar}>
          <Link
            to="/"
            onClick={handleLinkEvent}
            className={navigationStyles.sidebarLink}
            tabIndex={0}
          >
            Kalenteri
          </Link>
          <Link
            className={navigationStyles.sidebarLink}
            tabIndex={0}
            to="/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Raportit
          </Link>
          <Link
            className={navigationStyles.sidebarLink}
            tabIndex={0}
            to="/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Ilmoitukset
          </Link>
          <Link
            className={navigationStyles.sidebarLink}
            tabIndex={0}
            to="/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Sijaislista
          </Link>
          <button className={navigationStyles.sidebarLinkLogout} tabIndex={0}>
            <ExitIcon className={navigationStyles.exitIcon} />
            Log out
          </button>
        </Drawer.Body>
      </Drawer>
    </div>
  );
};

export default NavDropdownMobile;
