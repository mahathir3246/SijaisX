import { useState, useEffect } from 'react';
import { DateRangePicker, Loader, Message, toaster } from 'rsuite';
import { format } from 'date-fns';
import { get_teacher_classes_within_range } from '../../../functions/api_calls';
import styles from "../../../scss_stylings/postJobPopup.module.scss"
import { update_class_info } from '../../../functions/api_calls';
import ClassCard from './ClassCard';


export default function ScheduleJobMode({}) {
    const [range, setRange] = useState<[Date, Date] | null>(null);
    const [loading, setLoading] = useState(false);

    const datesInBetween = (start: Date, end:Date) => {
        const dates: Date[] = [];
        const current  = new Date(start)

        while(current<=end){
            dates.push(new Date(current));
            current.setDate(current.getDate()+1)
        }
        return dates;
    }



    return (
        <div>
            <div className={styles.dateSection}>
                <h6>Select the date/dates you want a substitute for:</h6>
                <DateRangePicker
                    className={styles.datePicker}
                    onChange={(value) => setRange(value as [Date, Date] | null)}
                    placeholder="Choose date or date range"
                    value={range}
                />
                {range?.map(date=>
                    <ClassCard/>
                )}
            </div>
        </div>
    );
}