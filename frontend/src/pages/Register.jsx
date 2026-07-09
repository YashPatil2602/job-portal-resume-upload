import React, {useState} from 'react'
import api from '../services/api'

export default function Register(){
  const [name,setName]=useState('')
  const [email,setEmail]=useState('')
  const [password,setPassword]=useState('')
  const [msg,setMsg]=useState('')

  const submit=async e=>{
    e.preventDefault()
    try{
      await api.post('/auth/register',{name,email,password})
      setMsg('Registered, please login')
    }catch(err){
      setMsg(err?.response?.data?.msg || 'Registration failed')
    }
  }

  return (
    <div style={{maxWidth:480}}>
      <h2>Register</h2>
      <form onSubmit={submit}>
        <div>
          <label>Name</label>
          <input value={name} onChange={e=>setName(e.target.value)} />
        </div>
        <div>
          <label>Email</label>
          <input value={email} onChange={e=>setEmail(e.target.value)} />
        </div>
        <div>
          <label>Password</label>
          <input type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        </div>
        <button type="submit">Register</button>
      </form>
      <div>{msg}</div>
    </div>
  )
}
