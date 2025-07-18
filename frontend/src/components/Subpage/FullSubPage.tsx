import NavigationBar from './Navbar/SubPageNavBar';
import Footer from './SubFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";
import SubstituteProfile from './Maincontent/subProfile';
import SubUpcomings from './Maincontent/SubUpcomings/subUpcomings';
import CalendarCard from './Maincontent/Calendar';
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
                            <SubstituteProfile/>       
                        </Col>

                        <Col xs={24} md={13}>
                            <div>
                                <div className={teacherstyles.jobPostHeadline}>
                                    <h3 className={teacherstyles.profile}>Your job posts</h3>
                                </div>
                                <SubUpcomings/>
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
