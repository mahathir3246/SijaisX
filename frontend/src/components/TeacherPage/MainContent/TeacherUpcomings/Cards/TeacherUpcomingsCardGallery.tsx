import { Grid, Row, Col } from 'rsuite';
import ClassCard from './ClassCard';
import styles from "../../../../../scss_stylings/card.module.scss"

import { jobs, Job } from '../../../Data/jobsdata';   // NEW

const TeacherUpcomingsCardGallery = () => (
  <div className={`${styles.galleryWrapper} ${styles.cardRail}`}>  
    <div className={styles.cardContainer}>
      {jobs.map((job: Job) => (
        <div
          key={job.class}
          className={styles.cardWrapper}
        >
          <ClassCard job={job} />
        </div>
      ))}
    </div>
  </div>
);

export default TeacherUpcomingsCardGallery;