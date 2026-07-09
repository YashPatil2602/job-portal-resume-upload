import React, {useEffect, useState} from 'react'
import { useParams, Link } from 'react-router-dom'
import api from '../services/api'

export default function JobDetails(){
  const {id} = useParams()
  const [job,setJob]=useState(null)

  useEffect(()=>{
    api.get(`/jobs/${id}`).then(r=>setJob(r.data))
  },[id])

  if(!job) return <div>Loading...</div>
  return (
    <div>
      <h2>{job.title}</h2>
      <p><strong>Company:</strong> {job.company}</p>
      <p><strong>Location:</strong> {job.location}</p>
      <p>{job.description}</p>
      <Link to={`/jobs/${id}/apply`}>Apply</Link>
    </div>
  )
}
