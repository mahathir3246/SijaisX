import 'rsuite/dist/rsuite.min.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import FullHomePage from "./pages/HomePage/FullHomePage";
import RegisterPage from './pages/Register/Register';
import Login from './pages/Login/Login';
import ProtectedRoute from './pages/Login/ProtectedRoute';
import TeacherDashboard from "./pages/TeacherPage/layout/TeacherDashboard";
import TeacherProfile from "./pages/TeacherPage/TeacherProfile/TeacherProfile";
import TeacherUpcomingsTable from "./pages/TeacherPage/UpcomingJobs(Teacher)/Table/TeacherJobsTable";
import SchoolJobsTable from "./pages/TeacherPage/UpcomingJobs(School)/Table/SchoolJobsTable";
import SubDashboard from './pages/SubPage/layout/SubDashboard';
import SubstituteProfile from './pages/SubPage/Profile/SubProfile';
import SubstituteJobListTable from './pages/SubPage/jobs/components/Table/SubstituteJobListTable';
import {
  get_batch_of_available_assignments_for_substitute,
  get_all_applied_batches_of_substitute,
  get_batch_of_accepted_assignments_for_substitute} 
from './functions/api_calls';
import PastJobs from './pages/TeacherPage/PastJobs/PastJobs';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FullHomePage/>} /> {/* Homepage content */}
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<Login />} />


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
              pageElemenTtoShow = {<SchoolJobsTable/>}/>
          }
        />

        <Route
          path="/teacher/past-jobs"
          element={
            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<PastJobs/>}/>
          }
        />

        <Route
          path="/substitute/dashboard"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<SubDashboard/>}/>}
        />

        <Route
          path="/substitute/profile"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<SubstituteProfile/>}/>}
        />

        <Route
          path="/substitute/available-jobs"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<SubstituteJobListTable apiFunction={get_batch_of_available_assignments_for_substitute}/>}/>}
        />

        <Route
          path="/substitute/applied-jobs"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<SubstituteJobListTable apiFunction={get_all_applied_batches_of_substitute}/>}/>}
        />

        <Route
          path="/substitute/accepted-jobs"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<SubstituteJobListTable apiFunction={get_batch_of_accepted_assignments_for_substitute}/>}/>}
        />

      </Routes>
    </Router>
  );
}

export default App;