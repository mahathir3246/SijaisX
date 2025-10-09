import { useState, useEffect, useCallback } from 'react';
import { Modal, Message, toaster, Button } from 'rsuite';
import ScheduleJobMode from './ScheduleJobMode';
import CustomJobs from './CustomClassForm';
import styles from "../../../scss_stylings/postJobPopup.module.scss"
import { getUserID } from '../../../functions/auth';
import { CustomJobData } from './CustomCLassCard';
import { create_batch_assignment, create_class, get_teacher_info } from '../../../functions/api_calls';
import { TeacherData } from '../MainContent/teacherProfile';


// Keep the interfaces for now (we'll move them later)
export interface ClassData {
    class_ID: string;
    subject: string;
    grade: string;
    beginning_time: string;
    ending_time: string;
    room: string;
}

export interface EditableClass extends ClassData {
    notes: string;
    isEditing: boolean;
    originalData: ClassData;
}

export interface Props { 
    open: boolean;
    onClose(): void;
}

export default function PostJobModal({ open, onClose }: Props) {
    // Add mode selection state
    const [mode, setMode] = useState<'schedule' | 'custom'>('schedule');
    const [scheduleClasses, setScheduleClasses] = useState<EditableClass[]>([]);
    const [customJobs, setCustomJobs] = useState<CustomJobData[]>([]);
    // Keep teacher ID logic

    const teacherID = getUserID() || "";

    // Reset state when modal opens/closes
    useEffect(() => {
        if (!open) {
            setMode('schedule');
            setScheduleClasses([]);
            setCustomJobs([]);
        }
    }, [open]);

    const handleCustomJobsUpdate = useCallback((jobs: CustomJobData[]) => {
        setCustomJobs(jobs);
    }, []);
    // Handle schedule classes update
    const handleScheduleClassesUpdate = useCallback((classes: EditableClass[]) => {
        setScheduleClasses(classes);
    }, []);

    // Handle mode change
    const handleModeChange = (newMode: 'schedule' | 'custom') => {
        setMode(newMode);
        setScheduleClasses([]);
    };

    //  handleSubmit logic
const handleSubmit = async() => {
    if (mode === 'schedule') {
        if (!scheduleClasses.length || !teacherID){
            toaster.push(<Message type='error'> No classes available to post assignments</Message>)
            return;
        }
        try{
            const assignments = scheduleClasses.map((cls)=>({
                class_ID: cls.class_ID,
                date: cls.beginning_time.slice(0,10),
                notes: cls.notes || "",
                status: "searching"
            }));
            console.log("Teacher ID:", teacherID);
            console.log("Schedule Assignments being sent:", assignments);
            const result = await create_batch_assignment(teacherID, assignments);

            if(result?.success){
                toaster.push(<Message type='success'>Successfully created {assignments.length} assignments from schedule</Message>);
                onClose()
            }else{
                toaster.push(<Message type='error'>Assignment creation failed</Message>)
            }

        }catch(error){
            console.log("Error: ",error)
        }
    } else if (mode === 'custom') {
    if (!customJobs.length || !teacherID){
        toaster.push(<Message type='error'> No custom jobs available to post assignments</Message>)
        return;
    }
    
    try{
        const teacherInfo = await get_teacher_info(teacherID) as TeacherData;
        const school_ID = teacherInfo.school_ID;
        // ✅ Step 1: Create real classes for each custom job
        const classCreationPromises = customJobs.map(async (job) => {
            const classData = {
                subject: job.subject,
                grade: job.grade,
                beginning_time: job.beginning_time,
                ending_time: job.ending_time,
                room: job.room,
                duration: 60,
                teacher_ID: teacherID,
                school_ID: school_ID
            };
            
            const result = await create_class(classData) as { success: boolean; class_ID: string }; // ✅ Type the result
            return result.class_ID;
        });
        
        const classIds = await Promise.all(classCreationPromises);
        
        // ✅ Step 2: Create assignments with real class IDs
        const assignments = customJobs.map((job, index) => ({
            class_ID: classIds[index],  // ✅ Use real class ID from database
            date: job.date,
            notes: job.notes || "",
            status: "searching"
        }));
        
        console.log("Teacher ID:", teacherID);
        console.log("Custom Assignments being sent:", assignments);
        const result = await create_batch_assignment(teacherID, assignments);

        if(result?.success){
            toaster.push(<Message type='success'>Successfully created {assignments.length} custom assignments</Message>);
            onClose()
        }else{
            toaster.push(<Message type='error'>Custom assignment creation failed</Message>)
        }

    }catch(error){
        console.log("Error: ",error)
        toaster.push(<Message type='error'>Error creating custom jobs</Message>)
    }
}
}

    return (
        <Modal size="lg" open={open} onClose={onClose} className={styles.modal}>
            <Modal.Header className={styles.header}>
                <h4>Post a Job</h4>
            </Modal.Header>

            <Modal.Body className={styles.body}>
                {/* Add your mode selection UI here */}
                <div className={styles.modeSelection}>
                    <button 
                        className={`${styles.modeButton} ${mode === 'schedule' ? styles.activeMode : styles.inactiveMode}`}
                        onClick={() => handleModeChange('schedule')}
                    >
                        📅 Use My Schedule
                    </button>
                    <button 
                        className={`${styles.modeButton} ${mode === 'custom' ? styles.activeMode : styles.inactiveMode}`}
                        onClick={() => handleModeChange('custom')}
                    >
                        ✏️ Create Custom Job
                    </button>
                </div>

                {/* Mode Content */}
                {mode === 'schedule' && (
                    <ScheduleJobMode 
                        onClassesUpdate={handleScheduleClassesUpdate}
                        teacherID={teacherID}
                    />
                )}

                {mode === 'custom' && (
                    <CustomJobs onJobsUpdate={handleCustomJobsUpdate}/>
                )}
            </Modal.Body>

            <Modal.Footer className={styles.footer}>
                <div className={styles.actions}>
                    <button className={styles.closeButton} onClick={onClose}>
                        Close
                    </button>
                    <Button
                        className={styles.saveButton}
                        onClick={handleSubmit}> 
                        Submit Assignment
                    </Button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}