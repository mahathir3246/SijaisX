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

export async function create_student(studentData: {
    name: string;
    phone_number: string;
    school_name: string;
    email: string;
    password: string;
}) {
    return await postData(`${BASE_URL}/student`, studentData);
}

export async function create_class(classData: {
    name: string;
    teacher_id: string;
}) {
    return await postData(`${BASE_URL}/class`, classData);
}

export async function create_feedback_to_teacher(feedbackData: {
    content: string;
    student_id: string;
    teacher_id: string;
}) {
    return await postData(`${BASE_URL}/feedback_to_teacher`, feedbackData);
}

export async function create_feedback_to_sub(feedbackData: {
    content: string;
    student_id: string;
    sub_id: string;
}) {
    return await postData(`${BASE_URL}/feedback_to_sub`, feedbackData);
}

export async function create_assignment(assignmentData: {
    title: string;
    description: string;
    class_id: string;
}) {
    return await postData(`${BASE_URL}/assignment`, assignmentData);
}

export async function create_preference(preferenceData: {
    student_id: string;
    class_id: string;
    preference: string;
}) {
    return await postData(`${BASE_URL}/preference`, preferenceData);
}

export async function create_availability(availabilityData: {
    teacher_id: string;
    start_time: string;
    end_time: string;
}) {
    return await postData(`${BASE_URL}/availability`, availabilityData);
}

export async function create_school(schoolData: {
    name: string;
    address: string;
    phone_number: string;
}) {
    return await postData(`${BASE_URL}/school`, schoolData);
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