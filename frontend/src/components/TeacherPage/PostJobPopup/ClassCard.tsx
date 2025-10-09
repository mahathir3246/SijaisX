import { Grid, Row, Col, Input } from 'rsuite';
import styles from '../../../scss_stylings/postJobPopup.module.scss';
import { EditableClass  } from './PostJobPopUp';


interface Props {
    classData: EditableClass;
    index: number; 
    onUpdateField: (index: number, field: string, value: string) => void;
    onStartEdit: (index: number) => void;
    onSaveChanges: (index: number) => void;
    onCancelEdit: (index: number) => void;
    isScheduleMode: boolean;
}

export default function ClassCard({ 
    classData, 
    index, 
    onUpdateField, 
    onStartEdit, 
    onSaveChanges, 
    onCancelEdit,
    isScheduleMode 
}: Props) {
    return (
        <div className={`${styles.classCard} ${classData.isEditing ? styles.editing : ''}`}>
            <Grid fluid>
                <Row gutter={16}>
                    {/* Subject field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Subject</label>
                            <Input
                                className={styles.input}
                                value={classData.subject}
                                onChange={(value) => onUpdateField(index, 'subject', value)}
                                disabled={!classData.isEditing}
                            />
                        </div>
                    </Col>
                    
                    {/* Grade field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Grade</label>
                            <Input
                                className={styles.input}
                                value={classData.grade}
                                onChange={(value) => onUpdateField(index, 'grade', value)}
                                disabled={!classData.isEditing}
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
                                value={classData.beginning_time.slice(11, 16)}
                                onChange={(value) => {
                                    // Keep the date part, replace the time part
                                    const date = classData.beginning_time.slice(0, 11);
                                    onUpdateField(index, 'beginning_time', date + value);
                                }}
                                disabled={!classData.isEditing}
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
                                value={classData.ending_time.slice(11, 16)}
                                onChange={(value) => {
                                    const date = classData.ending_time.slice(0, 11);
                                    onUpdateField(index, 'ending_time', date + value);
                                }}
                                disabled={!classData.isEditing}
                            />
                        </div>
                    </Col>
                    
                    {/* Room field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Room</label>
                            <Input
                                className={styles.input}
                                value={classData.room}
                                onChange={(value) => onUpdateField(index, 'room', value)}
                                disabled={!classData.isEditing}
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
                                value={classData.notes}
                                onChange={(value) => onUpdateField(index, 'notes', value)}
                                placeholder="Add any special instructions for the substitute..."
                                // Note: No disabled prop - always editable
                            />
                        </div>
                    </Col>
                </Row>
                
                {/* Button section - only show for schedule mode */}
                {isScheduleMode && (
                    <div className={styles.buttonSection}>
                        {/* If not editing, show Edit button */}
                        {!classData.isEditing ? (
                            <button
                                className={styles.editButton}
                                onClick={() => onStartEdit(index)}
                            >
                                ✏️ Edit Class Info
                            </button>
                        ) : (
                            // If editing, show Save and Cancel buttons
                            <>
                                <button
                                    className={styles.saveButton}
                                    onClick={() => onSaveChanges(index)}
                                >
                                    💾 Save Changes
                                </button>
                                <button
                                    className={styles.cancelButton}
                                    onClick={() => onCancelEdit(index)}
                                >
                                    ❌ Cancel
                                </button>
                            </>
                        )}
                    </div>
                )}
            </Grid>
        </div>
    );
}