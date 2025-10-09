import { Grid, Row, Col, Input } from 'rsuite';
import styles from '../../../scss_stylings/postJobPopup.module.scss';


export interface CustomJobData {
    subject: string;
    grade: string;
    beginning_time: string;
    ending_time: string;
    room: string;
    notes: string;
    date: string;
}


interface Props {
    jobData: CustomJobData;
    onUpdate: (updatedData: CustomJobData) => void;
}

export default function CustomClassCard({ jobData, onUpdate }: Props){
    
    // Update individual fields
    const updateField = (field: keyof CustomJobData, value: string) => {
        onUpdate({
            ...jobData,
            [field]: value
        });
    };

    return(
        <Grid fluid>
            <Row gutter={16}>
                {/* Subject field */}
                <Col xs={12} sm={6}>
                    <div className={styles.formGroup}>
                        <label className={styles.label}>Subject</label>
                        <Input
                            className={styles.input}
                            value={jobData.subject}
                            onChange={(value) => updateField('subject', value)}
                            placeholder="e.g., Mathematics"
                        />
                    </div>
                </Col>
                
                {/* Grade field */}
                <Col xs={12} sm={6}>
                    <div className={styles.formGroup}>
                        <label className={styles.label}>Grade *</label>
                        <Input
                            className={styles.input}
                            value={jobData.grade}
                            onChange={(value) => updateField('grade', value)}
                            placeholder="e.g., 7A"
                        />
                    </div>
                </Col>
                
                {/* Start time field */}
                <Col xs={12} sm={6}>
                    <div className={styles.formGroup}>
                        <label className={styles.label}>Start Time *</label>
                            <Input
                                className={`${styles.input} ${styles.timeInput}`}
                                type="time"
                                value={jobData.beginning_time.slice(11, 16)}
                                onChange={(value) => {
                                    const date = jobData.beginning_time.slice(0, 11);
                                    updateField('beginning_time', date + value);
                                }}
                            />
                    </div>
                </Col>
                
                {/* End time field */}
                <Col xs={12} sm={6}>
                    <div className={styles.formGroup}>
                        <label className={styles.label}>End Time *</label>
                            <Input
                                className={`${styles.input} ${styles.timeInput}`}
                                type="time"
                                value={jobData.ending_time.slice(11, 16)}
                                onChange={(value) => {
                                    const date = jobData.ending_time.slice(0, 11);
                                    updateField('ending_time', date + value);
                                }}
                            />
                    </div>
                </Col>
                
                {/* Room field */}
                <Col xs={12} sm={6}>
                    <div className={styles.formGroup}>
                        <label className={styles.label}>Room</label>
                        <Input
                            className={styles.input}
                            value={jobData.room}
                            onChange={(value) => updateField('room', value)}
                            placeholder="e.g., A101"
                        />
                    </div>
                </Col>
                
                {/* Notes field */}
                <Col xs={12} sm={6}>
                    <div className={`${styles.formGroup} ${styles.notesGroup}`}>
                        <label className={styles.label}>Notes</label>
                        <Input
                            as="textarea"
                            rows={2}
                            placeholder="Add any special instructions for the substitute..."
                            value={jobData.notes}
                            onChange={(value) => updateField('notes', value)}
                        />
                    </div>
                </Col>
            </Row>
        </Grid>
    )
}