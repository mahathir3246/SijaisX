"use client";
import ResponsiveNav from "@rsuite/responsive-nav";
import { Link } from 'react-router-dom';
import navigationStyles from "../../scss_stylings/navbar.module.scss";

const NavigationBarComponents = () => {
  return (
    <div className={navigationStyles.navContainer}>
      <ResponsiveNav
        id="responsiveNav"
        moreText="More"
        moreProps={{ className: navigationStyles.moreDropDownButton }}
        pullRight={true}
        className={navigationStyles.responsiveNav}
      >
        <ResponsiveNav.Item className={navigationStyles.navLink}>
          <p className={navigationStyles.navItemSubContainer}>Tietoa Meistä</p>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item className={navigationStyles.navLink}>
          <p className={navigationStyles.navItemSubContainer}>Ota yhteyttä</p>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          as={Link}
          to="/opettajille"
          className={navigationStyles.navLink}
        >
            <span className={navigationStyles.navItemSubContainer}>
                Opettajille
            </span> 
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          as={Link}
          to="/sijaisille"
          className={navigationStyles.navLink}
        >
          <span className={navigationStyles.navItemSubContainer}>Sijaisille</span>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          as={Link}
          to="/register"
          className={navigationStyles.navLink}
        >
          <span className={navigationStyles.register}>Hae SijaisX</span>
        </ResponsiveNav.Item>
        <ResponsiveNav.Item
          as={Link}
          to="/login"
          className={navigationStyles.navLink}
          
        >
          <span className={navigationStyles.login}>Kirjaudu sisään</span>
        </ResponsiveNav.Item>
      </ResponsiveNav>
    </div>
  );
};

export default NavigationBarComponents;
