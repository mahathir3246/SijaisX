import NavigationBar from './Navbar/teacherPageNavBar';
import Footer from './Footer/teacherFooter';
import globalstyles from "../../scss_stylings/globals.module.scss";
import TeacherProfile from './MainContent/teacherProfile';
import TeacherUpcomings from './MainContent/TeacherUpcomings/teacherUpcomings';
import SchoolUpcomings from './MainContent/schoolupcomings';
import CalendarCard from './MainContent/Calendar';
import teacherstyles from "../../scss_stylings/teacher.module.scss"
import { Grid,Col, Row, Button } from 'rsuite';
import { Plus } from '@rsuite/icons';
import { useState } from 'react';
import PostJobModal from "./PostJobModal"


 const FullHomePage = () => {

    const [open, setOpen] = useState(false);

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
                                <div className={teacherstyles.jobPostHeadline}>
                                    <h3 className={teacherstyles.profile}>Your job posts</h3>
                                    <Button
                                        size="lg"                   // bigger than the default md
                                        appearance="primary"
                                        color="blue"
                                        startIcon={<Plus />}        // ➕ icon to the left of the label  :contentReference[oaicite:0]{index=0}
                                        className={teacherstyles.postJobBtn}   // extra tweaks live in SCSS
                                        onClick={() => setOpen(true)}
                                    >
                                        Post a Job
                                    </Button>

                                    <PostJobModal open={open} onClose={() => setOpen(false)} />
                                </div>
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
