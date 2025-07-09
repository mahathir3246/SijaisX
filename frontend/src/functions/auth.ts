export interface UserData {
  user_ID: string;
  role: 'teacher' | 'substitute';
  email: string;
  loginTime: string;
}

// Check if user is logged in
export const isAuthenticated = (): boolean => {
  const userData = localStorage.getItem('sijaisx_user');
  if (!userData) return false;
  
  try {
    const user = JSON.parse(userData);
    // Check if login is not older than 24 hours (optional session expiry)
    const loginTime = new Date(user.loginTime);
    const now = new Date();
    const hoursDiff = (now.getTime() - loginTime.getTime()) / (1000 * 60 * 60);
    
    return hoursDiff < 24; // Session expires after 24 hours
  } catch {
    return false;
  }
};

// Get current user data
export const getCurrentUser = (): UserData | null => {
  const userData = localStorage.getItem('sijaisx_user');
  if (!userData) return null;
  
  try {
    return JSON.parse(userData);
  } catch {
    return null;
  }
};

// Logout user
export const logout = (): void => {
  localStorage.removeItem('sijaisx_user');
  // Redirect to home page
  window.location.href = '/';
};

// Check if user has specific role
export const hasRole = (role: 'teacher' | 'substitute'): boolean => {
  const user = getCurrentUser();
  return user ? user.role === role : false;
};

// Get user role
export const getUserRole = (): 'teacher' | 'substitute' | null => {
  const user = getCurrentUser();
  return user ? user.role : null;
};

// Get user ID
export const getUserID = (): string | null => {
  const user = getCurrentUser();
  return user ? user.user_ID : null;
};