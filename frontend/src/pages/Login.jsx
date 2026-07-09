import React, {useState} from 'react'
import api from '../services/api'

export default function Login(){
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [msg, setMsg] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    try{
      const res = await api.post('/auth/login',{email,password})
      localStorage.setItem('token', res.data.access_token)
      setMsg('Logged in')
    }catch(err){
      setMsg(err?.response?.data?.msg || 'Login failed')
    }
  }

  return (
    <div style={{maxWidth: 480}}>
      <h2>Login</h2>
      <form onSubmit={submit}>
        <div>
          <label>Email</label>
          <input value={email} onChange={e=>setEmail(e.target.value)} />
        </div>
        <div>
          <label>Password</label>
          <input type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        </div>
        <button type="submit">Login</button>
      </form>
      <div>{msg}</div>
    </div>
  )
}
