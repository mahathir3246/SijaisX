import 'rsuite/dist/rsuite.min.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import FullHomePage from "./components/HomePage/FullHomePage";
import FullSijaisPage from "./components/Subpage/FullSubPage";
import FullOpePage from "./components/TeacherPage/FullOpePage";
import RegisterPage from "./components/Register/registerpage"
import LogIn from './components/Login/login';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FullHomePage/>} /> {/* Homepage content */}
        
        {/* Protected route for substitutes only */}
        <Route 
          path="/sijaisille" 
          element={
            <ProtectedRoute requiredRole="substitute" children={<FullSijaisPage />} />
          } 
        />
        
        {/* Protected route for teachers only */}
        <Route 
          path="/opettajille" 
          element={
            <ProtectedRoute requiredRole="teacher" children={<FullOpePage />} />
          } 
        />
        
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LogIn />} />
      </Routes>
    </Router>
  );
}

export default App;