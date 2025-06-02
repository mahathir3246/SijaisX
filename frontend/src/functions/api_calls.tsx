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

export async function get_teacher_info(teacherID: string) {
    return await fetchData(`${BASE_URL}/teacher/${teacherID}`);
}

export async function get_student_info(studentID: string) {
    return await fetchData(`${BASE_URL}/student/${studentID}`);
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