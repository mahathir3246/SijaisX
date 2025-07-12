//This is like a "template" or "blueprint" for user information, 
// When someone logs in, we store their info in this exact format

export interface UserData{
    user_ID: string;
    role: 'teacher' | 'substitute';
    email: string;
}

//Check If Someone Is Logged In
export const isAuthenticated = (): boolean =>{

    //localStorage = Browser's storage (like a tiny database in the user's browser)
    // 'sijaisx-user' = The key we use to store user info (like a folder name)
    const userData = localStorage.getItem("sijaisx-user");

    if(!userData){
        return false;
    }

    try{
        const user = JSON.parse(userData)
        //This checks if ALL required pieces exist:
        return user && user.user_ID && user.role && user.email;
    }catch{
        return false;
    }

}

// Get current user data
export const getCurrentUser = (): UserData | null => {
    const userData = localStorage.getItem("sijaisx-user")
    if (!userData){
        return null;
    }
    try{
        const user = JSON.parse(userData)
        return user
    }catch{
        return null;
    }

}

export const logout = () =>{
    localStorage.removeItem("sijaisx-user")
    window.location.href = '/'   // Redirect to home page
}

export const hasRole = (role: 'teacher' | 'substitute'):boolean =>{
    const user = getCurrentUser()
    return user ? user.role === role : false;
}

export const getUserRole = (): 'teacher' | 'substitute' | null =>{
    const user = getCurrentUser();
    return user ? user.role : null;
}

export const getUserID = (): string | null =>{
    const user = getCurrentUser();
    return user ? user.user_ID : null;
}