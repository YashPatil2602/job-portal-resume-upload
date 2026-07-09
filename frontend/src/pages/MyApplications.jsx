import React, {useEffect, useState} from 'react'
import api from '../services/api'

export default function MyApplications(){
  const [apps,setApps]=useState([])

  useEffect(()=>{
    const token = localStorage.getItem('token')
    if(!token) return
    api.get('/applications', { headers: { Authorization: `Bearer ${token}` } }).then(r=>setApps(r.data)).catch(()=>{})
  },[])

  return (
    <div>
      <h2>My Applications</h2>
      <ul>
        {apps.map(a=> <li key={a.id}>{a.job_id} - {a.status}</li>)}
      </ul>
    </div>
  )
}
