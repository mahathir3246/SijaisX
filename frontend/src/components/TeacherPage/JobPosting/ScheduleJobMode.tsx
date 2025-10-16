import { useState, useEffect } from 'react';
import { Button, DateRangePicker } from 'rsuite';
import { format } from 'date-fns';
import { get_teacher_classes_within_range } from '../../../functions/api_calls';
import styles from "../../../scss_stylings/postJobPopup.module.scss";

import { create_batch_assignment } from '../../../functions/api_calls';
import ClassCard from './ClassCard';
import { getUserID } from '../../../functions/auth';

export interface ClassesBE{
    date: string,
    classes:{
        beginning_time: string,
        class_ID: string,
        ending_time: string,
        grade: string,
        room: string,
        subject: string
    }[]
}




export default function ScheduleJobMode({}) {
    const[classes, setClasses] = useState<{[date: string]: {
        beginning_time: string,
        class_ID: string,
        ending_time: string,
        grade: string,
        room: string,
        subject: string
    }[]}>({});
    const [range, setRange] = useState<[Date, Date] | null>(null);
    const [loading, setLoading] = useState(false);
    const [excludedClasses, setExcludedClasses] = useState<Set<string>>(new Set());
    const teacherId= getUserID();

    const datesInBetween = (start: Date, end:Date) => {
        const dates: Date[] = [];
        const current  = new Date(start)

        while(current<=end){
            dates.push(new Date(current));
            current.setDate(current.getDate()+1)
        }
        return dates;
    }

    useEffect(()=>{
        const fetchClasses = async () => {
            if (teacherId && range){
                const  start = format(range[0], 'yyyy-MM-dd HH:mm')
                const nextDay = new Date(range[1]);
                nextDay.setDate(nextDay.getDate() + 1);
                const end = format(nextDay,"'yyyy-MM-dd 00:00'")
                const result = await get_teacher_classes_within_range(teacherId,start,end)
                if (result && result.success){
                    setClasses(result.classes);
                }else {
                    console.error('Failed to fetch classes:', result?.error || 'Unknown error');
                    console.error('Result was:', result);
                    setClasses({});
                }
            }
        }
        fetchClasses()
    }, [range])

    const [assignmentNotes, setAssignmentNotes] = useState<{[key: string]: string}>({});

    const handleNotesChange = (classId: string, notes: string) => {
        setAssignmentNotes(prev => ({
            ...prev,
            [classId]: notes
        }));
    };

    const handleToggleExclude = (classId: string) => {
        setExcludedClasses(prev => {
            const newSet = new Set(prev);
            if (newSet.has(classId)) {
                newSet.delete(classId);
            } else {
                newSet.add(classId);
            }
            return newSet;
        });
    };

    const handleSubmit = async () => {
        if (!range) return;
        
        const teacherId = getUserID();
        if (!teacherId) {
            console.error('No teacher ID found');
            return;
        }

        try {
            const allAssignments: any[] = [];
            
            datesInBetween(range[0], range[1]).forEach((date) => {
                const classesForDate = classes[format(date, 'yyyy-MM-dd')];
                
                if (classesForDate) {
                    classesForDate.forEach((cls) => {
                        if (!excludedClasses.has(cls.class_ID)) {
                            allAssignments.push({
                                class_ID: cls.class_ID,
                                date: format(date, 'yyyy-MM-dd'),
                                notes: assignmentNotes[cls.class_ID] || "",
                                status: "searching"
                            });
                        }
                    });
                }
            });

            if (allAssignments.length === 0) {
                console.log('No classes to submit');
                return;
            }

            console.log('Submitting assignments:', allAssignments);
            
            // Call the API once with all assignments
            const result = await create_batch_assignment(teacherId, allAssignments);
            
            if (result && result.success) {
                console.log('Assignments created successfully');
            } else {
                console.error('Failed to create assignments:', result?.error);
            }
            
        } catch (error) {
            console.error('Error creating assignments:', error);
        }
    };


    return (
        <div className={styles.scheduleJobWrapper}>
            {/* Scrollable area for classes only */}
            <div className={styles.classesScrollArea}>
                <div className={styles.dateSection}>
                    <h6>Select the date/dates you want a substitute for:</h6>
                    <DateRangePicker
                        className={styles.datePicker}
                        onChange={(value) => setRange(value as [Date, Date] | null)}
                        placeholder="Choose date or date range"
                        value={range}
                    />
                    {loading && <div>Loading classes...</div>}
                    {range && datesInBetween(range[0], range[1]).map((date, dateIndex) => {
                        const classesForDate = classes[format(date, 'yyyy-MM-dd')];
                        
                        return (
                            <div key={dateIndex}>
                                <div className={styles.dateHeader}>
                                    <h6>{format(date, 'MMM dd, yyyy')}</h6>
                                </div>
                                {classesForDate?.map((cls, classIndex) => (
                                    <ClassCard 
                                        key={`${dateIndex}-${classIndex}`}
                                        class_ID={cls.class_ID}
                                        beginning_time={cls.beginning_time}
                                        ending_time={cls.ending_time}
                                        grade={cls.grade}
                                        room={cls.room}
                                        subject={cls.subject}
                                        notes=""
                                        duration={45}
                                        onNotesChange={handleNotesChange}
                                        onToggleExclude={() => handleToggleExclude(cls.class_ID)}
                                        isExcluded={excludedClasses.has(cls.class_ID)}
                                    />
                                ))}
                            </div>
                        );
                    })}
                </div>
            </div>
            
            {/* Fixed button area - outside scrollable content */}
            <div className={styles.fixedButtonArea}>
                <Button
                    className={styles.saveButton}
                    onClick={handleSubmit}
                > 
                    Submit Assignment
                </Button>
            </div>
        </div>
    );
}