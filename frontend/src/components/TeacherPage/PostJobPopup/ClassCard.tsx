import { Grid, Row, Col, Input } from 'rsuite';
import styles from '../../../scss_stylings/postJobPopup.module.scss';


export default function ClassCard({}) {
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
                            />
                        </div>
                    </Col>
                    
                    {/* Grade field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Grade</label>
                            <Input
                                className={styles.input}
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
                            />
                        </div>
                    </Col>
                    
                    {/* Room field */}
                    <Col xs={12} sm={6}>
                        <div className={styles.formGroup}>
                            <label className={styles.label}>Room</label>
                            <Input
                                className={styles.input}
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
                                // Note: No disabled prop - always editable
                            />
                        </div>
                    </Col>
                </Row>
                
            </Grid>
        </div>
    );
}