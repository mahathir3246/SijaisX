// CalendarCard.tsx
import { Calendar } from 'rsuite';
import styles from '../../../scss_stylings/substitute.module.scss';

export default function CalendarCard() {
  return (
    <div className={styles.frame}>
      <h2 className={styles.heading}>Calendar</h2>
      <Calendar
        compact                   // removes the right-hand sidebar
        isoWeek                   // Sunday-to-Saturday layout (matches screenshot)
        bordered
        className={styles.calendar}
        // onChange = {(date: Date) => setDate(date)}  <-- your own handler here
      />
    </div>
  );
}
