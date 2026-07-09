import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

export default function Applicants(){
  const {jobId} = useParams()
  const [apps,setApps]=useState([])

  useEffect(()=>{
    api.get(`/applications/job/${jobId}`).then(r=>setApps(r.data)).catch(()=>{})
  },[jobId])

  return (
    <div>
      <h2>Applicants for job {jobId}</h2>
      <ul>
        {apps.map(a=> (
          <li key={a.id}>{a.user_id} - <a href={a.resume_path}>Download</a></li>
        ))}
      </ul>
    </div>
  )
}
