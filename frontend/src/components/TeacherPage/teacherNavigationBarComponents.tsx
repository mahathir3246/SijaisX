"use client";
import ResponsiveNav from "@rsuite/responsive-nav";
import NoticeIcon from '@rsuite/icons/Notice';
import { useState } from "react";
import { Link } from 'react-router-dom';
import navigationStyles from "../../scss_stylings/navbar.module.scss";
import ExitIcon from "@rsuite/icons/Exit";
import PlusIcon from "@rsuite/icons/Plus";
import CreateSubstituteModal from "./CreateSubstituteModal";

const NavigationBarComponents = () => {
    const [openModal, setOpenModal] = useState(false); // State to control modal visibility
  return (
    <div className={navigationStyles.navContainer}>
      <ResponsiveNav
        id="responsiveNav"
        moreText="More"
        moreProps={{ className: navigationStyles.moreDropDownButton }}
        pullRight={true}
        className={navigationStyles.responsiveNav}
      >
        <ResponsiveNav.Item 
        className={navigationStyles.navLink}
        onClick={() => setOpenModal(true)}>
          <p className={navigationStyles.LuoSijaisuus}>
          <PlusIcon style={{ marginRight: "6px" }} />
          Luo Sijaisuus</p>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item className={navigationStyles.navLink}>
          <p className={navigationStyles.navItemSubContainer}>Kalenteri</p>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item className={navigationStyles.navLink}>
          <p className={navigationStyles.navItemSubContainer}>Raportit</p>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          as={Link}
          to="/"
          className={navigationStyles.navLink}
        >
            <span className={navigationStyles.navItemSubContainer}>
                <NoticeIcon style={{ marginRight: "6px" }} />
                Ilmoitukset
            </span> 
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          as={Link}
          to="/"
          className={navigationStyles.navLink}
        >
          <span className={navigationStyles.navItemSubContainer}>Sijaislista</span>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          className={`${navigationStyles.logOut} ${navigationStyles.navLink}`}
        >
          <p className={navigationStyles.navItemSubContainer}>
            <ExitIcon className={navigationStyles.exitIcon} />
            Kirjaudu ulos
          </p>
        </ResponsiveNav.Item>
        <CreateSubstituteModal open={openModal} onClose={() => setOpenModal(false)} />
      </ResponsiveNav>
    </div>
  );
};

export default NavigationBarComponents;
