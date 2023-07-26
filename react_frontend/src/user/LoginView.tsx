import React, { useState } from 'react'
import { authAPI } from '../auth/authAPI'

export default function LoginView(){
  const [userName, setUserName] = useState('')
  const [password, setPassword] = useState('')

  const handleLogin = async () => {
    console.log({ userName, password })
    await authAPI
      .login({ username: userName, password: password })
      .then(res => console.log(res))
      .catch(err => console.log(err))
  }

  return (
    <div>
      <input
        value={userName}
        onChange={event => setUserName(event.target.value)}
        // type='userName'
        placeholder='username'
      />
      <input
        value={password}
        onChange={event => setPassword(event.target.value)}
        type='password'
        placeholder='password'
      />
      <button type='submit' onClick={handleLogin}>
        login
      </button>
    </div>
  )
}
