import { Grid, Row, Col } from 'rsuite';
import ClassCard from './ClassCard';
import styles from "../../../../../scss_stylings/card.module.scss"

import { jobs, Job } from '../../../Data/jobsdata';   // NEW

const TeacherUpcomingsCardGallery = () => (
  <div className={styles.galleryWrapper}>
    <Grid>
      <Row gutter={32}>
        {jobs.map((job: Job) => (
          <Col key={job.class} xs={24} sm={12} md={8} lg={6}>
            <ClassCard job={job}/>
          </Col>

        ))}
      </Row>
    </Grid>

  </div>
);

export default TeacherUpcomingsCardGallery;
