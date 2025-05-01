"use client";
import { Link } from 'react-router-dom';
import navigationStyles from "../../scss_stylings/navbar.module.scss";
import NavDropdownMobile from "./SijaisDropdownmobile";
import NavigationBarComponents from "./SijaisNavBarComponents";

const NavigationBar = () => {
  return (
    <div className={navigationStyles.headerContainer}>
      <div className={navigationStyles.headerSubContainer}>
        <NavDropdownMobile />
        <Link className={navigationStyles.logoContainer} to="/">
          <div className={navigationStyles.logoSmall}>
            SijaisX 
          </div>
          <div className={navigationStyles.logoBig}>
            SijaisX
          </div>
        </Link>
        <NavigationBarComponents />
      </div>
    </div>
  );
};

export default NavigationBar;
