import ClassCard from './ClassCard';
import styles from "../../../../../scss_stylings/card.module.scss"
import { Job } from '../teacherUpcomings';


type GalleryProps = { jobs: Job[] };


export default function TeacherUpcomingsCardGallery({ jobs }: GalleryProps) {
  return(
    <div className={`${styles.galleryWrapper} ${styles.cardRail}`}>  
      <div className={styles.cardContainer}>
        {jobs.map((job) => (
          <div
            key={`${job.date}-${job.beginning_time}-${job.subject}`}
            className={styles.cardWrapper}
          >
            <ClassCard job={job} />
          </div>
        ))}
      </div>
    </div>
  )
};
