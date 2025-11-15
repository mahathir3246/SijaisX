import { ReactNode } from 'react';
import { Navigate } from 'react-router-dom';
import { isAuthenticated, getUserRole } from '../../functions/auth';



interface ProtectedRouteProps{
    requiredRole?: "teacher" | "substitute";
    pageElemenTtoShow: ReactNode;
    redirectTo?: string;
}

const ProtectedRoute = ({ 
  pageElemenTtoShow, 
  requiredRole, 
  redirectTo = "/login"
}: ProtectedRouteProps) => {
    
    if(!isAuthenticated()){
        return <Navigate to={redirectTo} replace/>
    }

    if (requiredRole){
        const userRole = getUserRole()
        if (requiredRole !== userRole){
            if (userRole === "teacher"){
                return <Navigate to = {"/opettajille"}  replace/>
            } else if (userRole ==="substitute") {
                return <Navigate to={"/sijaisille"} replace/>
            }else{ 
                return <Navigate to="/login" replace />;
        }
    }

    return pageElemenTtoShow;
    }

}

export default ProtectedRoute;
