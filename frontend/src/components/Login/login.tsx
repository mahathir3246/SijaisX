import navigationStyles from "../../scss_stylings/navbar.module.scss";
import Footer from '../HomePage/HomePageFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";
import LoginForm from "./loginForm";
const LogIn = () => {
    return(
        <div className={globalstyles.appContainer}>
            <div className={navigationStyles.registerHeaderContainer}>
                <div className={navigationStyles.registerlogocontainer}>
                    <div className={navigationStyles.logoSmall}>
                        SijaisX 
                    </div>
                    <div className={navigationStyles.logoBigRegister}>
                        SijaisX
                    </div>
                </div>
            </div>
            <LoginForm/>
            <Footer/>
        </div>
    )
}

export default LogIn