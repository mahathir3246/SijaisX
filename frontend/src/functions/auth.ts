export interface UserData {
  user_ID: string;
  role: 'teacher' | 'substitute';
  email: string;
}

// Check if user is logged in
export const isAuthenticated = (): boolean => {
  const userData = localStorage.getItem('sijaisx_user');
  if (!userData) return false;
  
  try {
    const user = JSON.parse(userData);
    // Simple check: if user data exists and has required fields, user is authenticated
    return user && user.user_ID && user.role && user.email;
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