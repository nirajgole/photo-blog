import { useState } from 'react'
import { authAPI } from '../auth/authAPI'
import { useAuth } from '../App'
import { useLocation, useNavigate } from 'react-router-dom'

export default function LoginView() {
  const [userName, setUserName] = useState('')
  const [password, setPassword] = useState('')
  const [successMessage, setSuccessMessage] = useState('')
  const { isLoggedIn, setIsLoggedIn } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()

  const handleLogin = async () => {
    if (isLoggedIn) return
    setIsLoggedIn(true)

    if (location.state?.from) {
      navigate(location.state.from)
    }
    console.log({ userName, password })
    await authAPI
      .login({ username: userName, password: password })
      .then(res => setSuccessMessage(res.data?.message))
      .catch(err => setSuccessMessage(err))
  }

  return (
    <div>
      {successMessage ? (
        <h1>{successMessage}</h1>
      ) : (
        <>
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
        </>
      )}
    </div>
  )
}
