import { ReactNode } from 'react';
import { Navigate } from 'react-router-dom';
import { isAuthenticated, getUserRole } from '../functions/auth';

interface ProtectedRouteProps {
  children: ReactNode;
  requiredRole?: 'teacher' | 'substitute';
  redirectTo?: string;
}

const ProtectedRoute = ({ 
  children, 
  requiredRole, 
  redirectTo = '/login' 
}: ProtectedRouteProps) => {
  // Check if user is authenticated
  if (!isAuthenticated()) {
    return <Navigate to={redirectTo} replace />;
  }

  // If a specific role is required, check if user has that role
  if (requiredRole) {
    const userRole = getUserRole();
    if (userRole !== requiredRole) {
      // Redirect to appropriate page based on user's actual role
      if (userRole === 'teacher') {
        return <Navigate to="/opettajille" replace />;
      } else if (userRole === 'substitute') {
        return <Navigate to="/sijaisille" replace />;
      } else {
        return <Navigate to="/login" replace />;
      }
    }
  }

  // User is authenticated and has the required role (if any)
  return <>{children}</>;
};

export default ProtectedRoute;