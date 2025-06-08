import NavigationBar from './teacherPageNavBar';
import Footer from './teacherFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";

 const FullHomePage = () => {

    return(
        <div className={globalstyles.appContainer}>
            <NavigationBar/>
            <main className={globalstyles.content}> {/* Your Page Content */} </main>
            <Footer/>
        </div>        
    )

  
}

export default FullHomePage;
