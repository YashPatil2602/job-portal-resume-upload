import React from 'react'
import { Link } from 'react-router-dom'

export default function NavBar(){
  return (
    <nav style={{padding: '1rem', borderBottom: '1px solid #ddd'}}>
      <Link to="/jobs" style={{marginRight: 12}}>Jobs</Link>
      <Link to="/applications" style={{marginRight: 12}}>My Applications</Link>
      <Link to="/admin/jobs" style={{marginRight: 12}}>Admin Jobs</Link>
      <Link to="/login" style={{float: 'right'}}>Login</Link>
    </nav>
  )
}
