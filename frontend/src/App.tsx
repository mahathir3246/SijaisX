import 'rsuite/dist/rsuite.min.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import FullHomePage from "./components/HomePage/FullHomePage";
import FullSijaisPage from "./components/Subpage/FullSubPage";
import RegisterPage from './components/Register/Register';
import Login from './components/Login/Login';
import ProtectedRoute from './components/Login/ProtectedRoute';
import TeacherDashboard from "./components/TeacherNew/TeacherDashboard";
import TeacherProfile from "./components/TeacherNew/TeacherProfile/TeacherProfile";
import TeacherUpcomingsTable from "./components/TeacherNew/UpcomingJobs(Teacher)/Table/TeacherUpcomings(table)";
import SchoolUpcomingsTable from "./components/TeacherNew/UpcomingJobs(School)/Table/SchoolUpcomingsTable";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FullHomePage/>} /> {/* Homepage content */}
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<Login />} />

        <Route
          path="/sijaisille"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<FullSijaisPage/>}/>}
        />


        <Route
          path="/teacher/dashboard"
          element={
            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<TeacherDashboard/>}/>
          }
        />

        <Route
          path="/teacher/profile"
          element={
            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<TeacherProfile/>}/>
          }
        />

        <Route
          path="/teacher/my-jobs"
          element={
            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<TeacherUpcomingsTable/>}/>
          }
        />
        <Route
          path="/teacher/school-jobs"
          element={
            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<SchoolUpcomingsTable/>}/>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;