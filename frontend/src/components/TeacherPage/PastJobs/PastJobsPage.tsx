
import NavigationBar from "../Navbar/teacherPageNavBar";
import Footer from "../Footer/teacherFooter";
import globalstyles from "../../../scss_stylings/globals.module.scss";

const PastJobsPage = () => {


    return(
        <div className={globalstyles.appContainer}>
            <NavigationBar/>
            <Footer/>
        </div>        
    )

  
}

export default PastJobsPage;
