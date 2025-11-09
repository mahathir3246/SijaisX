import 'rsuite/dist/rsuite.min.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import FullHomePage from "./components/HomePage/FullHomePage";
import FullSijaisPage from "./components/Subpage/FullSubPage";
import FullOpePage from "./components/TeacherPage/FullOpePage";
import RegisterPage from "./components/Register/registerpage"
import LogIn from './components/Login/login';
import ProtectedRoute from './components/Login/ProtectedRoute';
import PastJobsPage from "./components/TeacherPage/PastJobs/PastJobsPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FullHomePage/>} /> {/* Homepage content */}
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LogIn />} />

        <Route
          path="/sijaisille"
          element={
          <ProtectedRoute 
            requiredRole='substitute'
            pageElemenTtoShow ={<FullSijaisPage/>}/>}
        />

        <Route
          path = "/opettajille"
          element={

            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<FullOpePage/>}/>
          }
        />

        <Route
          path="/opettajille/past-jobs"
          element={
            <ProtectedRoute
              requiredRole='teacher'
              pageElemenTtoShow = {<PastJobsPage/>}/>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;