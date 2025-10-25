import { Grid, Row, Col, Input } from 'rsuite';
import styles from '../../../scss_stylings/postJobPopup.module.scss';
import { useState } from 'react';
import { update_class_info } from '../../../functions/api_calls';
import { getUserID } from '../../../functions/auth';


export interface ClassesFE{
    class_ID:string
    beginning_time: string,
    ending_time: string,
    grade: string,
    room: string,
    subject: string,
    notes: string,
    duration: number,
    onNotesChange?: (classId: string, notes: string) => void
    onToggleExclude?: () => void,
    isExcluded?: boolean

}



export default function ClassCard({
    class_ID,
    beginning_time,
    ending_time,
    grade,
    room,
    subject,
    notes,
    duration,
    onNotesChange,
    onToggleExclude,
    isExcluded = false

}: ClassesFE) {

    const[isEditing, setIsEditing] = useState<boolean>(false)
    const[editedValues, setEditedValues] = useState({
        subject: subject,
        grade: grade,
        beginning_time: beginning_time,
        ending_time: ending_time,
        room: room,
        notes: notes,
        duration: duration
    })

    const handelEdit = (field:string, value:string) =>{
        setEditedValues(prev=>({
            ...prev,
            [field]:value
        }))
        if (field === 'notes' && onNotesChange) {
            onNotesChange(class_ID, value);
        }
    } 

    const handleSave = () => {
        const hasChanges = 
            editedValues.subject !== subject ||
            editedValues.grade !== grade ||
            editedValues.beginning_time !== beginning_time ||
            editedValues.ending_time !== ending_time ||
            editedValues.room !== room ||
            editedValues.notes !== notes ||
            editedValues.duration !== duration;

        if (!hasChanges) {
            console.log('No changes to save');
            setIsEditing(false);
            return;
        }
        const teacherID= getUserID()
        if(teacherID){
        update_class_info(class_ID, teacherID, {
            subject: editedValues.subject,
            grade: editedValues.grade,
            beginning_time: editedValues.beginning_time,
            ending_time: editedValues.ending_time,
            duration: editedValues.duration,
            room: editedValues.room
        })
        }
        setIsEditing(false)
    }

    const handleCancel= () =>{
        setEditedValues(prev =>({
            subject: subject,
            grade: grade,
            beginning_time: beginning_time,
            ending_time: ending_time,
            room: room,
            notes: notes,
            duration:duration
        }))
        setIsEditing(false)
    }
    return (
        <div className={`${styles.classCard}`}>
            <Grid fluid>
                <Row gutter={16}>
                    {/* Subject field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Subject</label>
                            <Input
                                className={styles.input}
                                value={editedValues.subject}
                                disabled={!isEditing}
                                onChange={value=>handelEdit("subject", value)}

                            />
                        </div>
                    </Col>

                    {/* Grade field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Grade</label>
                            <Input
                                className={styles.input}
                                value={editedValues.grade}
                                disabled={!isEditing}
                                onChange={value=>handelEdit("grade", value)}
                            />
                        </div>
                    </Col>

                    {/* Start time field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Start Time</label>
                            <Input
                                className={`${styles.input} ${styles.timeInput}`}
                                type="time"
                                value={editedValues.beginning_time.slice(11,16)}
                                disabled={!isEditing}
                                onChange={value=>{
                                    const datePart = editedValues.beginning_time.slice(0, 10)  // Use editedValues, not beginning_time
                                    const newTime = `${datePart} ${value}`
                                    handelEdit("beginning_time", newTime)
                                }}
                            />
                        </div>
                    </Col>

                    {/* End time field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>End Time</label>
                            <Input
                                className={`${styles.input} ${styles.timeInput}`}
                                type="time"
                                value={editedValues.ending_time.slice(11,16)}
                                disabled={!isEditing}
                                onChange={value=>{
                                    const datePart = editedValues.ending_time.slice(0, 10)  // Use editedValues, not beginning_time
                                    const newTime = `${datePart} ${value}`
                                    handelEdit("ending_time", newTime)
                                }}
                            />
                        </div>
                    </Col>

                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Duration</label>
                            <Input
                                className={`${styles.input}`}
                                type="number"
                                value={editedValues.duration}
                                disabled={!isEditing}
                                onChange={value=>handelEdit("duration", value)}
                            />
                        </div>
                    </Col>

                    {/* Room field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Room</label>
                            <Input
                                className={styles.input}
                                value={editedValues.room}
                                disabled={!isEditing}
                                onChange={value=>handelEdit("room", value)}
                            />
                        </div>
                    </Col>

                    {/* Notes field - always editable (for Assignment table) */}
                    <Col xs={12} sm={6}>
                        <div className={`${styles.formGroup} ${styles.notesGroup}`}>
                            <label className={styles.label}>Notes</label>
                            <Input
                                as="textarea"
                                rows={2}
                                className={`${styles.input} ${styles.textarea}`}
                                placeholder="Add any special instructions for the substitute..."
                                value={editedValues.notes}
                                onChange={value=>handelEdit("notes", value)}
                            />
                        </div>
                    </Col>
                </Row>
                <div className={styles.buttonSection}>
                    {/* Delete/Restore button */}
                    {onToggleExclude && (
                        <button
                            className={isExcluded ? styles.restoreButton : styles.deleteButton}
                            onClick={onToggleExclude}
                        >
                            {isExcluded ? '↩️ Restore' : '🗑️ Exclude'}
                        </button>
                    )}
    
                    {/* If not editing, show Edit button */}
                    {!isEditing ? (
                        <button
                            className={styles.editButton}
                            onClick={()=>setIsEditing(true)}
                        >
                            ✏️ Edit Class Info
                        </button>
                    ) : (
                        // If editing, show Save and Cancel buttons
                        <>
                            <button
                                className={styles.saveButton}
                                onClick={handleSave}
                            >
                                💾 Save Changes
                            </button>
                            <button
                                className={styles.cancelButton}
                                onClick={handleCancel}
                            >
                                ❌ Cancel
                            </button>
                        </>
                    )}
                </div>

            </Grid>
        </div>
    );
}
