import NavigationBar from './Navbar/teacherPageNavBar';
import Footer from './Footer/teacherFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";
import TeacherProfile from './MainContent/teacherProfile';
import TeacherUpcomings from './MainContent/TeacherUpcomings/teacherUpcomings';
import SchoolUpcomings from './MainContent/schoolupcomings';
import CalendarCard from './MainContent/Calendar';
import teacherstyles from "../../scss_stylings/teacher.module.scss"
import { Grid,Col, Row } from 'rsuite';

 const FullHomePage = () => {

    return(
        <div className={globalstyles.appContainer}>
            <NavigationBar/>
            <main className={globalstyles.content}> 
                <Grid 
                fluid
                className={teacherstyles.fullLayout}
                >
                    <Row gutter={32} style={{ alignItems: 'stretch' }}>
                        <Col xs={24} md={5} >
                            <TeacherProfile/>       
                        </Col>

                        <Col xs={24} md={13}>
                            <div>
                                <h3 className={teacherstyles.profile}>Your job posts</h3>
                                <TeacherUpcomings/>
                            </div>
                            
                            <div style={{ marginTop: '30px' }}>
                                <h3 className={teacherstyles.midheadline}>Upcoming substitutes</h3>
                                <SchoolUpcomings/>
                            </div>
                        </Col>

                        <Col xs={24} md={5}>
                            <CalendarCard/>
                        </Col>
                    </Row>
                </Grid>
            </main>
            <Footer/>
        </div>        
    )

  
}

export default FullHomePage;
