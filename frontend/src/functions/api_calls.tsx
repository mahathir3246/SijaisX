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

// Function to update assignment status in the API
export async function update_assignment_status(assignmentID: string, updatedData: {
    date?: string;
    notes?: string;
    status?: string;
    class_ID?: string;
    teacher_ID?: string;
    substitute_ID?: string;
}) {
    try {
        const response = await fetch(`${BASE_URL}/assignment/${assignmentID}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updatedData),
        });
        if (!response.ok) {
            console.error(`PUT /assignment/${assignmentID} failed:`, await response.text());
            return null;
        }
        return await response.json();
    } catch (err) {
        console.error(`PUT /assignment/${assignmentID} failed:`, err);
        return null;
    }
}


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