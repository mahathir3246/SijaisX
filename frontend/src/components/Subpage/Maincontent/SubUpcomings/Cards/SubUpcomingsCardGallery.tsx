import ClassCard from './ClassCard';
import styles from "../../../../../scss_stylings/card.module.scss";
import { SubstitutionFE } from '../SubstituteJobLists';

interface GalleryProps {
    substitutions: SubstitutionFE[];
}

const SubUpcomingsCardGallery = ({ substitutions }: GalleryProps) => {
    return (
        <div className={`${styles.galleryWrapper} ${styles.substituteCardRail}`}>  
            <div className={styles.substituteCardContainer}>
                {substitutions.map((substitution, index) => (
                    <div
                        key={`${substitution.date}-${substitution.school_name}-${substitution.teacher_name}-${index}`}
                        className={styles.cardWrapper}
                    >
                        <ClassCard substitution={substitution} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SubUpcomingsCardGallery;