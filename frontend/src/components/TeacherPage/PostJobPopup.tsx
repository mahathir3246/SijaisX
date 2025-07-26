import { useState, useEffect } from 'react';
import { Modal, DateRangePicker, Grid, Row, Col, Input, Loader, Message, toaster } from 'rsuite';
import { format } from 'date-fns';
import { get_teacher_classes_within_range, update_class_info, create_batch_assignment } from '../../functions/api_calls';
import styles from '../../scss_stylings/postJobPopup.module.scss';

// TypeScript interface defining the structure of class data from the database
interface ClassData {
    class_ID: string;        // Unique identifier for the class
    subject: string;         // Subject name (e.g., "Mathematics")
    grade: string;          // Grade level (e.g., "7A")
    beginning_time: string; // Start time in format "2025-07-21 08:15"
    ending_time: string;    // End time in format "2025-07-21 09:00"
    room: string;           // Room number/name (e.g., "A101")
}

// Extended interface that adds UI-specific fields to ClassData
interface EditableClass extends ClassData {
    notes: string;          // Notes for the substitute (goes to Assignment table)
    isEditing: boolean;     // Whether this class is currently being edited
    originalData: ClassData; // Backup of original values for cancel functionality
}

// Props interface defining what the parent component passes to this modal
interface Props { 
    open: boolean;          // Whether the modal is visible
    onClose(): void;        // Function to call when modal should be closed
}


export default function PostAssignmentModal({ open, onClose }: Props) {

    const [range, setRange] = useState<[Date, Date] | null>(null);
    const [classes, setClasses] = useState<EditableClass[]>([]);
    const [loading, setLoading] = useState(false);
    const [submitting, setSubmitting] = useState(false);

    // AUTHENTICATION - Get teacher ID from browser's localStorage
    // This data was stored when the teacher logged in
    const userData = JSON.parse(localStorage.getItem("sijaisx-user") || "{}");
    const teacherID = userData.user_ID; // Extract teacher's unique ID

    // EFFECT 1: Reset modal state when opened/closed
    // This runs whenever the 'open' prop changes
    useEffect(() => {
        // If modal is being closed, clear all data for a fresh start next time
        if (!open) {
            setRange(null);      // Clear selected date range
            setClasses([]);      // Clear fetched classes
            setSubmitting(false); // Reset submitting state
        }
    }, [open]); // Dependency array - only run when 'open' changes

    // EFFECT 2: Fetch classes when date range or teacher changes
    // This runs whenever range or teacherID changes
    useEffect(() => {
        // Early return if we don't have both required values
        if (!range || !teacherID) return;

        // Async function to fetch classes from the API
        const fetchClasses = async () => {
            setLoading(true); // Show loading spinner
            try {
                // Destructure the date range array into start and end dates
                const [startDate, endDate] = range;
                
                // Format start date to include time (keep original time from date picker)
                const start = format(startDate, 'yyyy-MM-dd HH:mm');
                
                // For end date, add 1 day to include the full last day
                // This fixes the issue where selecting 21.07-22.07 would miss 22.07 classes
                const nextDay = new Date(endDate);
                nextDay.setDate(nextDay.getDate() + 1); // Add one day
                const end = format(nextDay, 'yyyy-MM-dd 00:00'); // Set to midnight of next day
                
                // Call our API function to get teacher's classes in the date range
                const result = await get_teacher_classes_within_range(teacherID, start, end);
                
                // Check if the API call was successful and returned classes
                if (result?.success && result.classes) {
                    // Transform the basic ClassData into EditableClass objects
                    const editableClasses: EditableClass[] = result.classes.map((cls: ClassData) => ({
                        ...cls,                    // Spread all original class properties
                        notes: '',                 // Initialize empty notes
                        isEditing: false,          // Start in non-editing mode
                        originalData: { ...cls }   // Save a copy of original data for cancel functionality
                    }));
                    
                    // Update state with the transformed classes
                    setClasses(editableClasses);
                    
                    // Show success message to user
                    toaster.push(<Message type="success">{`Found ${result.classes.length} classes`}</Message>);
                } else {
                    // No classes found - show info message and clear classes array
                    toaster.push(<Message type="info">No classes found for selected dates</Message>);
                    setClasses([]);
                }
            } catch (error) {
                // Handle any errors that occur during the API call
                console.error("Error fetching classes:", error);
                toaster.push(<Message type="error">Failed to fetch classes</Message>);
                setClasses([]); // Clear classes on error
            } finally {
                // Always hide loading spinner, whether success or error
                setLoading(false);
            }
        };

        // Call the async function
        fetchClasses();
    }, [range, teacherID]); // Dependencies - run when either range or teacherID changes

    // HELPER FUNCTION: Group classes by date for organized display
    const groupClassesByDate = (classes: EditableClass[]) => {
        // Create an object where keys are date strings and values are arrays of classes
        const grouped: { [date: string]: EditableClass[] } = {};
        
        // Process each class
        classes.forEach(cls => {
            // Extract just the date part from beginning_time
            // "2025-07-21 08:15" becomes "2025-07-21"
            const date = cls.beginning_time.slice(0, 10);
            
            // If this is the first class for this date, create an empty array
            if (!grouped[date]) {
                grouped[date] = [];
            }
            
            // Add this class to the array for its date
            grouped[date].push(cls);
        });
        
        // Sort classes within each date by their start time
        Object.keys(grouped).forEach(date => {
            // Sort alphabetically by beginning_time (works because of ISO format)
            grouped[date].sort((a, b) => a.beginning_time.localeCompare(b.beginning_time));
        });
        
        return grouped; // Return the organized object
    };

    // HELPER FUNCTION: Format date string for display headers
    const formatDateHeader = (dateString: string) => {
        // Convert date string to Date object
        const date = new Date(dateString);
        // Format as "21.07.2025 (Monday)" using date-fns
        return format(date, 'dd.MM.yyyy (EEEE)');
    };

    // EVENT HANDLER: Update a specific field of a specific class
    const updateClassField = (index: number, field: string, value: string) => {
        // Update classes state using functional update pattern
        setClasses(prev => 
            // Map through all classes
            prev.map((cls, i) => 
                // If this is the class we want to update
                i === index 
                    ? { ...cls, [field]: value } // Create new object with updated field
                    : cls                         // Otherwise, keep the class unchanged
            )
        );
    };

    // EVENT HANDLER: Start editing mode for one class, stop editing for all others
    const startEdit = (index: number) => {
        // Update classes state
        setClasses(prev => 
            // Map through all classes
            prev.map((c, i) => 
                i === index 
                    ? { ...c, isEditing: true }   // Set the current values and Enable editing for target class
                    : { ...c, isEditing: false }  // Set the current values and Disable editing for all other classes
            )
        );
    };

    // EVENT HANDLER: Save changes to a class (updates database immediately)
    const saveClassChanges = async (index: number) => {
        // Get the specific class being saved
        const cls = classes[index];
        
        try {
            // Build an object containing only the fields that changed
            const classUpdates: any = {}; // Object to store changed fields
            let hasUpdates = false;        // Flag to track if anything actually changed

            // Compare each field with its original value
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

            // Only make API call if there are actual changes
            if (hasUpdates) {
                // Debug logging
                console.log("Updating class:", cls.class_ID, classUpdates);
                
                // Call API to update the class in the database
                const result = await update_class_info(cls.class_ID, teacherID, classUpdates);
                
                // If update was successful
                if (result) {
                    // Update local state to reflect the saved changes
                    setClasses(prev => 
                        prev.map((c, i) => 
                            i === index 
                                ? { 
                                    ...c, 
                                    isEditing: false, // Exit edit mode
                                    // Update originalData to match current values
                                    originalData: {
                                        class_ID: c.class_ID,
                                        subject: c.subject,
                                        grade: c.grade,
                                        beginning_time: c.beginning_time,
                                        ending_time: c.ending_time,
                                        room: c.room
                                    }
                                }
                                : c // Leave other classes unchanged
                        )
                    );
                    // Show success message
                    toaster.push(<Message type="success">Class updated successfully</Message>);
                } else {
                    // API call failed
                    toaster.push(<Message type="error">Failed to update class</Message>);
                }
            } else {
                // No changes were made, just exit edit mode
                setClasses(prev => 
                    prev.map((c, i) => 
                        i === index ? { ...c, isEditing: false } : c
                    )
                );
                // Inform user that nothing was changed
                toaster.push(<Message type="info">No changes to save</Message>);
            }
        } catch (error) {
            // Handle any errors during the save process
            console.error("Error updating class:", error);
            toaster.push(<Message type="error">Error updating class</Message>);
        }
    };

    // EVENT HANDLER: Cancel editing and revert all changes
    const cancelEdit = (index: number) => {
        setClasses(prev => 
            prev.map((c, i) => 
                i === index 
                    ? { 
                        ...c, 
                        isEditing: false, // Exit edit mode
                        // Restore all fields to their original values
                        subject: c.originalData.subject,
                        grade: c.originalData.grade,
                        beginning_time: c.originalData.beginning_time,
                        ending_time: c.originalData.ending_time,
                        room: c.originalData.room
                    }
                    : c // Leave other classes unchanged
            )
        );
    };

    // EVENT HANDLER: Post assignments for selected classes
    const postAssignments = async () => {
        // Validate that we have classes and teacher ID
        if (!classes.length || !teacherID) {
            toaster.push(<Message type="error">No classes available to post assignments for</Message>);
            return;
        }

        setSubmitting(true);
        try {
            // Create assignment data for each class
            const assignmentData = classes.map(cls => ({
                class_ID: cls.class_ID,
                date: cls.beginning_time.slice(0, 10), // Extract date part (YYYY-MM-DD)
                notes: cls.notes || '', // Use notes or empty string
                status: 'searching' // Default status for new assignments
            }));

            // Call the batch assignment API
            const result = await create_batch_assignment(teacherID, assignmentData);

            if (result?.success) {
                toaster.push(<Message type="success">{result.message || `Successfully posted ${assignmentData.length} assignments!`}</Message>);
                // Close the modal after successful submission
                onClose();
            } else {
                toaster.push(<Message type="error">{result?.error || 'Failed to post assignments'}</Message>);
            }
        } catch (error) {
            console.error('Error posting assignments:', error);
            toaster.push(<Message type="error">Error occurred while posting assignments</Message>);
        } finally {
            setSubmitting(false);
        }
    };

    // RENDER SECTION
    return (
        // Main modal container with size and visibility controls
        <Modal size="lg" open={open} onClose={onClose} className={styles.modal}>
            {/* Modal header with title */}
            <Modal.Header className={styles.header}>
                <h4>Post Assignments</h4>
            </Modal.Header>

            {/* Main modal content area */}
            <Modal.Body className={styles.body}>
                {/* Date selection section */}
                <div className={styles.dateSection}>
                    <h6>Select the date/dates you want to post assignments for:</h6>
                    <DateRangePicker
                        className={styles.datePicker}
                        // When user selects dates, update our range state
                        onChange={(value) => setRange(value as [Date, Date] | null)}
                        placeholder="Choose date or date range"
                        value={range} // Controlled component - state controls the value
                    />
                </div>

                {/* Loading state - show spinner while fetching classes */}
                {loading && (
                    <div className={styles.loadingContainer}>
                        <Loader size="md" content="Loading classes..." />
                    </div>
                )}

                {/* Classes display section - only show if not loading and have classes */}
                {!loading && classes.length > 0 && (
                    <div className={styles.classesSection}>
                        <h6>Classes for selected dates:</h6>
                        
                        {/* Complex data transformation and rendering chain */}
                        {Object.entries(groupClassesByDate(classes))
                            // Convert grouped object to array of [date, classes] pairs
                            .sort(([dateA], [dateB]) => dateA.localeCompare(dateB)) // Sort dates chronologically
                            .map(([date, dayClasses]) => ( // Render each date group
                                <div key={date} className={styles.dayGroup}>
                                    {/* Date header showing day and class count */}
                                    <div className={styles.dateHeader}>
                                        <h5>{formatDateHeader(date)}</h5>
                                        <span className={styles.classCount}>
                                            {dayClasses.length} classes
                                        </span>
                                    </div>
                                    
                                    {/* Container for all classes on this date */}
                                    <div className={styles.dayClasses}>
                                        {dayClasses.map((cls) => {
                                            // Find this class's position in the original array
                                            // We need this for the update functions
                                            const originalIndex = classes.findIndex(c => c.class_ID === cls.class_ID);
                                            
                                            return (
                                                <div 
                                                    key={cls.class_ID} 
                                                    // Dynamic className based on editing state
                                                    className={`${styles.classCard} ${cls.isEditing ? styles.editing : ''}`}
                                                >
                                                    {/* RSuite Grid system for responsive layout */}
                                                    <Grid fluid>
                                                        <Row gutter={16}>
                                                            {/* Subject field */}
                                                            <Col xs={12} sm={6}>
                                                                <div className={styles.formGroup}>
                                                                    <label className={styles.label}>Subject</label>
                                                                    <Input
                                                                        className={styles.input}
                                                                        value={cls.subject} // Controlled input
                                                                        // Update state when user types
                                                                        onChange={(value) => updateClassField(originalIndex, 'subject', value)}
                                                                        disabled={!cls.isEditing} // Only editable when in edit mode
                                                                    />
                                                                </div>
                                                            </Col>
                                                            
                                                            {/* Grade field */}
                                                            <Col xs={12} sm={6}>
                                                                <div className={styles.formGroup}>
                                                                    <label className={styles.label}>Grade</label>
                                                                    <Input
                                                                        className={styles.input}
                                                                        value={cls.grade}
                                                                        onChange={(value) => updateClassField(originalIndex, 'grade', value)}
                                                                        disabled={!cls.isEditing}
                                                                    />
                                                                </div>
                                                            </Col>
                                                            
                                                            {/* Start time field */}
                                                            <Col xs={12} sm={6}>
                                                                <div className={styles.formGroup}>
                                                                    <label className={styles.label}>Start Time</label>
                                                                    <Input
                                                                        className={`${styles.input} ${styles.timeInput}`}
                                                                        type="time" // HTML5 time picker
                                                                        // Extract time part (HH:MM) from full timestamp
                                                                        value={cls.beginning_time.slice(11, 16)}
                                                                        onChange={(value) => {
                                                                            // Keep the date part, replace the time part
                                                                            const date = cls.beginning_time.slice(0, 11);
                                                                            updateClassField(originalIndex, 'beginning_time', date + value);
                                                                        }}
                                                                        disabled={!cls.isEditing}
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
                                                                        value={cls.ending_time.slice(11, 16)}
                                                                        onChange={(value) => {
                                                                            const date = cls.ending_time.slice(0, 11);
                                                                            updateClassField(originalIndex, 'ending_time', date + value);
                                                                        }}
                                                                        disabled={!cls.isEditing}
                                                                    />
                                                                </div>
                                                            </Col>
                                                            
                                                            {/* Room field */}
                                                            <Col xs={12} sm={6}>
                                                                <div className={styles.formGroup}>
                                                                    <label className={styles.label}>Room</label>
                                                                    <Input
                                                                        className={styles.input}
                                                                        value={cls.room}
                                                                        onChange={(value) => updateClassField(originalIndex, 'room', value)}
                                                                        disabled={!cls.isEditing}
                                                                    />
                                                                </div>
                                                            </Col>
                                                            
                                                            {/* Notes field - always editable (for Assignment table) */}
                                                            <Col xs={12} sm={6}>
                                                                <div className={`${styles.formGroup} ${styles.notesGroup}`}>
                                                                    <label className={styles.label}>Notes</label>
                                                                    <Input
                                                                        as="textarea" // Multi-line input
                                                                        rows={2}
                                                                        className={`${styles.input} ${styles.textarea}`}
                                                                        value={cls.notes}
                                                                        onChange={(value) => updateClassField(originalIndex, 'notes', value)}
                                                                        placeholder="Add any special instructions for the substitute..."
                                                                        // Note: No disabled prop - always editable
                                                                    />
                                                                </div>
                                                            </Col>
                                                        </Row>
                                                        
                                                        {/* Button section - changes based on editing state */}
                                                        <div className={styles.buttonSection}>
                                                            {/* If not editing, show Edit button */}
                                                            {!cls.isEditing ? (
                                                                <button
                                                                    className={styles.editButton}
                                                                    onClick={() => startEdit(originalIndex)}
                                                                >
                                                                    ✏️ Edit Class Info
                                                                </button>
                                                            ) : (
                                                                // If editing, show Save and Cancel buttons
                                                                <>
                                                                    <button
                                                                        className={styles.saveButton}
                                                                        onClick={() => saveClassChanges(originalIndex)}
                                                                    >
                                                                        💾 Save Changes
                                                                    </button>
                                                                    <button
                                                                        className={styles.cancelButton}
                                                                        onClick={() => cancelEdit(originalIndex)}
                                                                    >
                                                                        ❌ Cancel
                                                                    </button>
                                                                </>
                                                            )}
                                                        </div>
                                                    </Grid>
                                                </div>
                                            );
                                        })}
                                    </div>
                                </div>
                            ))}
                    </div>
                )}

                {/* Empty state - show when no classes found */}
                {!loading && classes.length === 0 && range && (
                    <div className={styles.emptyState}>
                        <div className={styles.icon}>📅</div>
                        No classes found for the selected date range.
                    </div>
                )}
            </Modal.Body>

            {/* Modal footer with action buttons */}
            <Modal.Footer className={styles.footer}>
                <div className={styles.actions}>
                    {/* Show Post Assignments button only when classes are available */}
                    {!loading && classes.length > 0 && (
                        <button 
                            className={styles.postButton} 
                            onClick={postAssignments}
                            disabled={submitting}
                        >
                            {submitting ? '📤 Posting...' : '📤 Post Assignments'}
                        </button>
                    )}
                    <button className={styles.closeButton} onClick={onClose} disabled={submitting}>
                        Close
                    </button>
                </div>
            </Modal.Footer>
        </Modal>
    );
}