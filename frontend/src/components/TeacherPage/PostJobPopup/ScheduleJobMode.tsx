import { useState, useEffect } from 'react';
import { DateRangePicker, Loader, Message, toaster } from 'rsuite';
import { format } from 'date-fns';
import { get_teacher_classes_within_range } from '../../../functions/api_calls';
import styles from "../../../scss_stylings/postJobPopup.module.scss"
import { update_class_info } from '../../../functions/api_calls';
import ClassCard from './ClassCard';
import { ClassData, EditableClass } from './PostJobPopUp';



interface Props {
    onClassesUpdate: (classes: EditableClass[]) => void;
    teacherID: string;
}

export default function ScheduleJobMode({ onClassesUpdate, teacherID }: Props) {
    const [range, setRange] = useState<[Date, Date] | null>(null);
    const [classes, setClasses] = useState<EditableClass[]>([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!range || !teacherID) return;

        const fetchClasses = async () => {
            setLoading(true);
            try {
                const [startDate, endDate] = range;
                const start = format(startDate, 'yyyy-MM-dd HH:mm');
                const nextDay = new Date(endDate);
                nextDay.setDate(nextDay.getDate() + 1);
                const end = format(nextDay, 'yyyy-MM-dd 00:00');
                
                const result = await get_teacher_classes_within_range(teacherID, start, end);
                
                if (result?.success && result.classes) {
                    const editableClasses: EditableClass[] = result.classes.map((cls: ClassData) => ({
                        ...cls,
                        notes: '',
                        isEditing: false,
                        originalData: { ...cls }
                    }));
                    
                    setClasses(editableClasses);
                    toaster.push(<Message type="success">{`Found ${result.classes.length} classes`}</Message>);
                } else {
                    toaster.push(<Message type="info">No classes found for selected dates</Message>);
                    setClasses([]);
                }
            } catch (error) {
                console.error("Error fetching classes:", error);
                toaster.push(<Message type="error">Failed to fetch classes</Message>);
                setClasses([]);
            } finally {
                setLoading(false);
            }
        };

        fetchClasses();
    }, [range, teacherID]); 

    useEffect(() => {
        onClassesUpdate(classes);
    }, [classes, onClassesUpdate]);

    const groupClassesByDate = (classes: EditableClass[]) => {
        const grouped: { [date: string]: EditableClass[] } = {};
        
        classes.forEach(cls => {
            const date = cls.beginning_time.slice(0, 10);
            if (!grouped[date]) {
                grouped[date] = [];
            }
            grouped[date].push(cls);
        });
        
        Object.keys(grouped).forEach(date => {
            grouped[date].sort((a, b) => a.beginning_time.localeCompare(b.beginning_time));
        });
        
        return grouped;
    };

    const formatDateHeader = (dateString: string) => {
        const date = new Date(dateString);
        return format(date, 'dd.MM.yyyy (EEEE)');
    };

    const updateClassField = (index: number, field: string, value: string) => {
        setClasses(prev => {
            const updated = prev.map((cls, i) => 
                i === index ? { ...cls, [field]: value } : cls
            );
            return updated;
        });
    };

    const startEdit = (index: number) => {
        setClasses(prev => {
            const updated = prev.map((c, i) => 
                i === index ? { ...c, isEditing: true } : { ...c, isEditing: false }
            );
            return updated;
        });
    };

    const saveClassChanges = async (index: number) => {
        const cls = classes[index];
        
        try {
            const classUpdates: any = {};
            let hasUpdates = false;

            if (cls.subject !== cls.originalData.subject) {
                classUpdates.subject = cls.subject;
                hasUpdates = true;
            }
            if (cls.grade !== cls.originalData.grade) {
                classUpdates.grade = cls.grade;
                hasUpdates = true;
            }
            if (cls.beginning_time !== cls.originalData.beginning_time) {
                classUpdates.beginning_time = cls.beginning_time;
                hasUpdates = true;
            }
            if (cls.ending_time !== cls.originalData.ending_time) {
                classUpdates.ending_time = cls.ending_time;
                hasUpdates = true;
            }
            if (cls.room !== cls.originalData.room) {
                classUpdates.room = cls.room;
                hasUpdates = true;
            }

            if (hasUpdates) {
                console.log("Updating class:", cls.class_ID, classUpdates);
                
                const result = await update_class_info(cls.class_ID, teacherID, classUpdates);
                
                if (result) {
                    setClasses(prev => {
                        const updated = prev.map((c, i) => 
                            i === index ? { 
                                ...c, 
                                isEditing: false,
                                originalData: {
                                    class_ID: c.class_ID,
                                    subject: c.subject,
                                    grade: c.grade,
                                    beginning_time: c.beginning_time,
                                    ending_time: c.ending_time,
                                    room: c.room
                                }
                            } : c
                        );
                        return updated;
                    });
                    toaster.push(<Message type="success">Class updated successfully</Message>);
                } else {
                    toaster.push(<Message type="error">Failed to update class</Message>);
                }
            } else {
                setClasses(prev => {
                    const updated = prev.map((c, i) => 
                        i === index ? { ...c, isEditing: false } : c
                    );
                    return updated;
                });
                toaster.push(<Message type="info">No changes to save</Message>);
            }
        } catch (error) {
            console.error("Error updating class:", error);
            toaster.push(<Message type="error">Error updating class</Message>);
        }
    };

    const cancelEdit = (index: number) => {
        setClasses(prev => {
            const updated = prev.map((c, i) => 
                i === index ? { 
                    ...c, 
                    isEditing: false,
                    subject: c.originalData.subject,
                    grade: c.originalData.grade,
                    beginning_time: c.originalData.beginning_time,
                    ending_time: c.originalData.ending_time,
                    room: c.originalData.room
                } : c
            );
            return updated;
        });
    };

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
            </div>

            {loading && (
                <div className={styles.loadingContainer}>
                    <Loader size="md" content="Loading classes..." />
                </div>
            )}

            {!loading && classes.length > 0 && (
                <div className={styles.classesSection}>
                    <h6>Classes for selected dates:</h6>
                    
                    {Object.entries(groupClassesByDate(classes))
                        .sort(([dateA], [dateB]) => dateA.localeCompare(dateB))
                        .map(([date, dayClasses]) => (
                            <div key={date} className={styles.dayGroup}>
                                <div className={styles.dateHeader}>
                                    <h5>{formatDateHeader(date)}</h5>
                                    <span className={styles.classCount}>
                                        {dayClasses.length} classes
                                    </span>
                                </div>
                                
                                <div className={styles.dayClasses}>
                                    {dayClasses.map((cls) => {
                                        const originalIndex = classes.findIndex(c => c.class_ID === cls.class_ID);
                                        
                                        return (
                                            <ClassCard
                                                key={cls.class_ID}
                                                classData={cls}
                                                index={originalIndex}
                                                onUpdateField={updateClassField}
                                                onStartEdit={startEdit}
                                                onSaveChanges={saveClassChanges}
                                                onCancelEdit={cancelEdit}
                                                isScheduleMode={true}
                                            />
                                        );
                                    })}
                                </div>
                            </div>
                        ))}
                </div>
            )}


            {!loading && classes.length === 0 && range && (
                <div className={styles.emptyState}>
                    <div className={styles.icon}>📅</div>
                    No classes found for the selected date range.
                </div>
            )}
        </div>
    );
}