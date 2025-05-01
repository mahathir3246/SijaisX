import React from "react";
import 'rsuite/dist/rsuite.min.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import FullHomePage from "./components/HomePage/FullHomePage";
import FullSijaisPage from "./components/Subpage/FullSijaisPage";
import FullOpePage from "./components/TeacherPage/FullOpePage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<FullHomePage/>} /> {/* Homepage content */}
        <Route path="/sijaisille" element={<FullSijaisPage />} />
        <Route path="/opettajille" element={<FullOpePage />} />
      </Routes>
    </Router>
  );
}

export default App;