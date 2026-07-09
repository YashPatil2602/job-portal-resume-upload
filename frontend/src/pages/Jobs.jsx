import React, {useEffect, useState} from 'react'
import { Link } from 'react-router-dom'
import api from '../services/api'

export default function Jobs(){
  const [jobs,setJobs]=useState([])
  const [q,setQ]=useState('')

  async function fetchJobs(){
    const res = await api.get('/jobs',{params: {q}})
    setJobs(res.data)
  }

  useEffect(()=>{fetchJobs()},[])

  return (
    <div>
      <h2>Jobs</h2>
      <div>
        <input placeholder="Search" value={q} onChange={e=>setQ(e.target.value)} />
        <button onClick={fetchJobs}>Search</button>
      </div>
      <ul>
        {jobs.map(j=> (
          <li key={j.id}>
            <Link to={`/jobs/${j.id}`}>{j.title} - {j.company}</Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
