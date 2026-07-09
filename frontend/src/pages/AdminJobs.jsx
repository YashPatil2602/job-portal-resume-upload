import React, {useEffect, useState} from 'react'
import api from '../services/api'
import { Link } from 'react-router-dom'

export default function AdminJobs(){
  const [jobs,setJobs]=useState([])

  useEffect(()=>{ api.get('/jobs').then(r=>setJobs(r.data)) },[])

  return (
    <div>
      <h2>Admin Jobs</h2>
      <Link to="/admin/jobs/new">Add Job</Link>
      <ul>
        {jobs.map(j=> <li key={j.id}>{j.title} - <Link to={`/admin/applicants/${j.id}`}>Applicants</Link></li>)}
      </ul>
    </div>
  )
}
