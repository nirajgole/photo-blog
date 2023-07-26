import { useState } from 'react'
import client, { authAPI } from './auth/authAPI'

const App = () => {
  const [userName, setUserName] = useState('')
  const [password, setPassword] = useState('')

  const handleLogin = async () => {
    console.log({ userName, password })
    // const username = userName
    // await authAPI
    //   .login({ username, password })
    //   .then(res => console.log(res))
    //   .catch(err => console.error(err))
    const formData = new FormData()
    formData.append('username', userName)
    formData.append('password', password)
    await client.post('/login', { data: formData }).then(res => alert(res.data))
    // try {
    //   const response = await authAPI.login({ userName, password })
    //   console.log(response)
    //   const cookies = response.headers['set-cookie']
    //   console.log(cookies)
    // } catch (err) {
    //   console.error(err)
    // }
  }

  return (
    <div className='App'>
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

export default App
