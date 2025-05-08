import navigationStyles from "../../scss_stylings/navbar.module.scss";
import Footer from '../HomePage/HomePageFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";
import TeacherRegistrationForm from "./TeacherRegistrationForm"

const RegisterPage = () =>{
    return(
        <div className={globalstyles.appContainer}>
            <div className={navigationStyles.registerHeaderContainer}>
                <div className={navigationStyles.registerlogocontainer}>
                    <div className={navigationStyles.logoSmall}>
                        SijaisX 
                    </div>
                    <div className={navigationStyles.logoBig}>
                        SijaisX
                    </div>
                </div>
            </div>
            <TeacherRegistrationForm/>
            <Footer/>
        </div>
        

    )
}

export default RegisterPage;
