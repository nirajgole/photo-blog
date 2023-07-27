import React from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../App'

export default function HeaderView() {
  const { isLoggedIn, setIsLoggedIn} = useAuth();

  const handleLogOut=()=>{
    setIsLoggedIn(false)
  }
  return (
    <div>
      <nav
        style={{
          display: 'flex',
          justifyContent: 'space-around',
          justifyItems: 'left'
        }}
      >
        <Link to='/'>
          <button type='button'>Landing</button>
        </Link>

        <Link to='home' >
          <button type='button'>Home</button>
        </Link>

        {isLoggedIn ? (
          <Link to='/' onClick={handleLogOut}>
            <button type='button'>Logout</button>
          </Link>
        ) : (
          <Link to='login'>
            <button type='button'>Login</button>
          </Link>
        )}
      </nav>
    </div>
  )
}
