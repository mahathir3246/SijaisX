import NavigationBar from './Navbar/SubPageNavBar';
import Footer from './SubFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";
import SubstituteProfile from './Maincontent/subProfile';
import SubstituteJobLists from './Maincontent/SubUpcomings/SubstituteJobLists';
import CalendarCard from './Maincontent/Calendar';
import teacherstyles from "../../scss_stylings/teacher.module.scss"
import { Grid,Col, Row } from 'rsuite';
import { get_batch_of_available_assignments_for_substitute, get_batch_of_assignments_for_substitute } from '../../functions/api_calls';



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
                                    <h3 className={teacherstyles.profile}>Available Jobs</h3>
                                </div>
                                <SubstituteJobLists
                                    apiFunction={get_batch_of_available_assignments_for_substitute}/>
                                
                                <div className={teacherstyles.jobPostHeadline}>
                                    <h3 className={teacherstyles.profile}>Applied Jobs</h3>
                                </div>
                                <SubstituteJobLists
                                    apiFunction={get_batch_of_available_assignments_for_substitute}/>

                                <div className={teacherstyles.jobPostHeadline}>
                                    <h3 className={teacherstyles.profile}>Accepted Jobs</h3>
                                </div>
                                <SubstituteJobLists 
                                    apiFunction={get_batch_of_assignments_for_substitute}
                                />
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
