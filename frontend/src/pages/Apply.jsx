import React, {useState} from 'react'
import { useParams } from 'react-router-dom'
import api from '../services/api'

export default function Apply(){
  const {id} = useParams()
  const [file,setFile]=useState(null)
  const [msg,setMsg]=useState('')

  const submit = async e =>{
    e.preventDefault()
    const token = localStorage.getItem('token')
    if(!token){ setMsg('Login required'); return }
    const form = new FormData()
    form.append('job_id', id)
    form.append('resume', file)
    try{
      const res = await api.post('/applications/apply', form, { headers: { 'Content-Type': 'multipart/form-data', Authorization: `Bearer ${token}` } })
      setMsg('Applied')
    }catch(err){
      setMsg(err?.response?.data?.msg || 'Apply failed')
    }
  }

  return (
    <div style={{maxWidth:480}}>
      <h2>Apply</h2>
      <form onSubmit={submit}>
        <div>
          <label>Resume (PDF)</label>
          <input type="file" accept="application/pdf" onChange={e=>setFile(e.target.files[0])} />
        </div>
        <button type="submit">Submit Application</button>
      </form>
      <div>{msg}</div>
    </div>
  )
}
