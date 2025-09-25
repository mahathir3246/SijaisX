const BASE_URL = "http://localhost:5000/api";

async function fetchData<T>(url: string): Promise<T | null> {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Error fetching data from ${url}:`, response.statusText);
            return null;
        }
        const data: T = await response.json();
        return data;
    }
    catch (err){
        console.error(`Error fetching data from ${url}:`, err);
        return null;
    }
}

async function postData<T>(url: string, body: any): Promise<T | null> {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        });

        if (!response.ok) {
            console.error(`POST ${url} failed:`, await response.text());
            return null;
        }

        return await response.json();
    } catch (err) {
        console.error(`POST ${url} failed:`, err);
        return null;
    }
}


// Functions to fetch data from API
export async function get_teacher_info(teacherID: string) {
    return await fetchData(`${BASE_URL}/teacher/${teacherID}`);
}

export async function get_substitute_info(substituteID: string) {
    return await fetchData(`${BASE_URL}/substitute/${substituteID}`);
}

export async function get_class_info(classID: string) {
    return await fetchData(`${BASE_URL}/class/${classID}`);
}

export async function get_feedback_to_teacher(feedbackID: string) {
    return await fetchData(`${BASE_URL}/feedback_to_teacher/${feedbackID}`);
}

export async function get_feedback_to_sub(feedbackID: string) {
    return await fetchData(`${BASE_URL}/feedback_to_sub/${feedbackID}`);
}

export async function get_assignment_info(assignmentID: string) {
    return await fetchData(`${BASE_URL}/assignment/${assignmentID}`);
}

export async function preference_info(preferenceID: string) {
    return await fetchData(`${BASE_URL}/preference/${preferenceID}`);
}  

export async function get_availability_info(availabilityID: string) {
    return await fetchData(`${BASE_URL}/availability/${availabilityID}`);
}

export async function get_school_info(school_ID: string) {
    return await fetchData(`${BASE_URL}/school/${school_ID}`);
}

// this is to get volunteers for a particular assignment
export async function get_assignment_volunteers(assignmentID: string) {
    return await fetchData<{ volunteers: { substitute_ID: string, name: string, email: string }[] }>(
        `${BASE_URL}/assignments/${assignmentID}/volunteers`
    );
}

// function to get classes for a specific teacher of a specific range
export async function get_teacher_classes_within_range(teacher_ID: string, start_date: string, end_date: string) {
    const url = `${BASE_URL}/get_specifications/teacher_classes/${teacher_ID}?start_date=${start_date}&end_date=${end_date}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch classes: ${response.statusText}`);
            return null;
        }

        const data = await response.json();

        // Optional: Validate data shape     chatgpt
        if (!Array.isArray(data.classes)) {
            console.error("Unexpected data format:", data);
            return null;
        }

        return data;

    } catch (error) {
        console.error("Network or parsing error:", error);
        return null;
    }
}

// Funtion to get all assignments of a teacher
export async function get_all_assignments_of_teacher(teacher_ID: string | null){
    const url = `${BASE_URL}/get_specifications/all_assignments_teacher/${teacher_ID}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch all assignments: ${response.statusText}`);
            return null;
        }

        const data = await response.json();

        return data;
    } catch (error) {
        console.error("Connection error:", error);
        return null;
    }
}

// Funtion to get all assignments of a school
export async function get_all_assignments_of_school(school_ID: string){
    const url = `${BASE_URL}/get_specifications/all_assignments_school/${school_ID}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch all assignments: ${response.statusText}`);
            return null;
        }

        const data = await response.json();

        return data;
    } catch (error) {
        console.error("Connection error:", error);
        return null;
    }
}

// Function to get all assignments available to sub
export async function get_all_assignments_available_to_sub(substitute_ID: string) {
    const url = `${BASE_URL}/get_specifications/all_assignments_to_substitute/${substitute_ID}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch all assignments available to sub: ${response.statusText}`);
            return null; 
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Connection error:", error);
        return null;
    }
}

// Funtion to get all schools of a substitute
export async function get_all_schools_of_substitute(substitute_ID: string) {
    const url = `${BASE_URL}/get_specifications/all_schools_of_substitute/${substitute_ID}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch all schools of sub: ${response.statusText}`);
            return null; 
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Connection error:", error);
        return null;
    }
}

// Function to get batch of assigned assignments of a substitute
export async function get_batch_of_assignments_for_substitute(substitute_ID: string) {
    const url = `${BASE_URL}/get_specifications/get_accepted_batch_for_substitute/${substitute_ID}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch batch of assigned assignments of sub: ${response.statusText}`);
            return null; 
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Database connection error:", error);
        return null;
    }
}

// Function to get batch of available assignments of a substitute
export async function get_batch_of_available_assignments_for_substitute(substitute_ID: string) {
    const url = `${BASE_URL}/get_specifications/get_available_batch_for_substitute/${substitute_ID}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`Failed to fetch batch of available assignments of sub: ${response.statusText}`);
            return null; 
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Database connection error:", error);
        return null;
    }
}

// Functions to post data to API
export async function create_teacher(teacherData: {
    name: string;
    phone_number: string;
    school_name: string;
    email: string;
    password: string;
}) {
    return await postData(`${BASE_URL}/teacher`, teacherData);
}

export async function create_substitute(substituteData: {
    name: string;
    phone_number: string;
    email: string;
    password: string;
    experience: number;
}) {
    return await postData(`${BASE_URL}/substitute`, substituteData);
}

export async function create_class(classData: {
    subject: string;
    grade: string;
    beginning_time: string;
    ending_time: string;
    teacher_ID: string;
    room: string;
    school_ID: string;
}) {
    return await postData(`${BASE_URL}/class`, classData);
}

export async function create_feedback_to_teacher(feedbackData: {
    date: string;
    comments: string;
    teacher_ID: string;
    substitute_ID: string;
}) {
    return await postData(`${BASE_URL}/feedback_to_teacher`, feedbackData);
}

export async function create_feedback_to_sub(feedbackData: {
    date: string;
    rating: number;
    comments: string;
    teacher_ID: string;
    substitute_ID: string;
}) {
    return await postData(`${BASE_URL}/feedback_to_sub`, feedbackData);
}

export async function create_assignment(assignmentData: {
    date: string;
    notes: string;
    status: string;
    class_ID: string;
    teacher_ID: string;
    substitute_ID: string;
}) {
    return await postData(`${BASE_URL}/assignment`, assignmentData);
}

export async function create_preference(preferenceData: {
    grade: string;
    substitute_ID: string;
    school_name: string;
    subject: string;
    location: string;
}) {
    return await postData(`${BASE_URL}/preference`, preferenceData);
}

export async function create_availability(availabilityData: {
    substitute_ID: string;
    beginning_date: string;
    ending_date: string;
    location: string;
}) {
    return await postData(`${BASE_URL}/availability`, availabilityData);
}

export async function create_school(schoolData: {
    school_name: string;
}) {
    return await postData(`${BASE_URL}/school`, schoolData);
}   

export async function volunteer_in_school(teacher_ID: string, substitute_ID: string)
{
    return await postData(`${BASE_URL}/substitute_coordinator/${teacher_ID}/add_substitute_to_list`, { substitute_ID });
}

// Function to create batch assignments
export async function create_batch_assignment(
    teacher_ID: string,
    assignments: {
        class_ID: string;
        date: string;
        notes?: string;
        status?: string;
    } []
) {
    try {
        const response = await fetch(`${BASE_URL}/assignments/create_batch`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ teacher_ID, assignments }),
        });
        if (!response.ok) {
            console.error(`POST /assignments/create_batch failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`POST /assignments/create_batch failed:`, err);
        return null;
    }
}

// Function to add sub to school list
export async function add_substitute_to_school_list(teacher_ID: string, substitute_ID: string) {
    try {
        const response = await fetch(`${BASE_URL}/substitute_coordinator/${teacher_ID}/add_substitute_to_list`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ substitute_ID }),
        });
        if (!response.ok) {
            console.error(`POST /substitute_coordinator/${teacher_ID}/add_substitute_to_list failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`POST /substitute_coordinator/${teacher_ID}/add_substitute_to_list failed:`, err);
        return null;
    }
}

// Function to add substitute to assignment list
export async function add_substitute_to_assignment_list(assignmentID: string, substituteID: string) {
    try {
        const response = await fetch(`${BASE_URL}/assignments/${assignmentID}/volunteer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ substitute_ID: substituteID }),
        });
        if (!response.ok) {
            console.error(`POST /assignments/${assignmentID}/volunteer failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`POST /assignments/${assignmentID}/volunteer failed:`, err);
        return null;
    }
}

// Function to add substitute to batch of assignments
export async function add_substitute_to_assignment_batch(substituteID: string, assignmentBatch: string[]) {
    const formattedBatch = assignmentBatch.map(id => ({ assignment_ID: id }));
    try {
        const response = await fetch(`${BASE_URL}/assignments/volunteer_batch`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ substitute_ID: substituteID, assignment_batch: formattedBatch }),
        });
        if (!response.ok) {
            console.error(`POST /assignments/volunteer_batch failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`POST /assignments/volunteer_batch failed:`, err);
        return null;
    }
}

// Function to update assignment status in the API
export async function update_assignment_status(assignmentID: string, updatedData: {
        teacher_ID: string;
        status: string;
        substitute_ID?: string; // Only required for "accepted"
    }
) {
    try {
        const response = await fetch(`${BASE_URL}/assignments/${assignmentID}/status`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updatedData),
        });
        if (!response.ok) {
            console.error(`PATCH /assignments/${assignmentID}/status failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`PATCH /assignments/${assignmentID}/status failed:`, err);
        return null;
    }
}

// Function to update teacher profile
export async function update_teacher_profile(teacherID: string, updatedData: {
    name?: string;
    phone_number?: string;
    email?: string;
    password?: string;
    
}) {
    try {
        const response = await fetch(`${BASE_URL}/edit_profile/teacher/${teacherID}`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(updatedData),
        });
        if (!response.ok) {
            console.error(`PATCH /edit_profile/teacher/${teacherID} failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`PATCH /edit_profile/teacher/${teacherID} failed:`, err);
        return null;
    }
}

// Function to update substitute profile
export async function update_substitute_profile(substituteID: string, updatedData: {
    name?: string;
    phone_number?: string;
    email?: string;
    password?: string;
    experience?: number;
    highest_education?: string;
}) {
    try {
        const response = await fetch(`${BASE_URL}/edit_profile/substitute/${substituteID}`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(updatedData),
        });
        if (!response.ok) {
            console.error(`PATCH /edit_profile/substitute/${substituteID} failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`PATCH /edit_profile/substitute/${substituteID} failed:`, err);
        return null;
    }
}

// Function to update class info
export async function update_class_info(classID: string, teacherID: string, updatedData: {
    subject?: string;
    grade?: string;
    beginning_time?: string;
    ending_time?: string;
    duration?: number;
    room?: string;
}) {
    try {
        const response = await fetch(`${BASE_URL}/edit_class/${classID}`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({teacher_ID: teacherID, ...updatedData}),
        });
        if (!response.ok) {
            console.error(`PATCH /edit_class/${classID} failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`PATCH /edit_class/${classID} failed:`, err);
        return null;
    }
}

// Function to delete assignment(s)
export async function delete_assignments(
    teacher_ID: string,
    assignment_ids: string[]
) {
    if (!assignment_ids || assignment_ids.length === 0) {
        console.warn("No assignment IDs provided for deletion");
        return null;
    }

    try {
        const response = await fetch(`${BASE_URL}/assignments/delete`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ teacher_ID, assignment_ids }),
        });

        if (!response.ok) {
            console.error(`DELETE /assignments/delete failed:`, await response.text());
            return null;
        }

        const result = await response.json();

        if (result.success) {
            console.log(`Deleted ${result.deleted_count} assignments:`, result.deleted_ids);
        }

        return result;

    } catch (err) {
        console.error(`DELETE /assignments/delete failed:`, err);
        return null;
    }
}


// login function
export async function login(email: string, password: string) {
    try {
        const response = await fetch(`${BASE_URL}/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({email, password})
        })
        if (!response.ok){
            console.error('Error logging in:', response.statusText);
            return null;
        }
        return await response.json();
    
    } catch (error) {
        console.error('Error logging in:', error);
        return null;
    }
    
}