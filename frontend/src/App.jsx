import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import NavBar from './components/NavBar'
import Login from './pages/Login'
import Register from './pages/Register'
import Jobs from './pages/Jobs'
import JobDetails from './pages/JobDetails'
import Apply from './pages/Apply'
import MyApplications from './pages/MyApplications'
import AdminJobs from './pages/AdminJobs'
import Applicants from './pages/Applicants'

export default function App(){
  return (
    <div>
      <NavBar />
      <main style={{padding: '1rem'}}>
        <Routes>
          <Route path="/" element={<Navigate to="/jobs" />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/jobs" element={<Jobs />} />
          <Route path="/jobs/:id" element={<JobDetails />} />
          <Route path="/jobs/:id/apply" element={<Apply />} />
          <Route path="/applications" element={<MyApplications />} />
          <Route path="/admin/jobs" element={<AdminJobs />} />
          <Route path="/admin/applicants/:jobId" element={<Applicants />} />
        </Routes>
      </main>
    </div>
  )
}
