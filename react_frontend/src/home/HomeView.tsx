import { useEffect, useState } from 'react'
import client from '../auth/authAPI'
import { User } from '../user/userModel'

export default function HomeView() {
  const [users, setUsers] = useState<User[]>([])

  useEffect(() => {
    const getUsers = async () => {
      return await client
        .get('/users')
        .then(res => setUsers(res.data))
        .catch(err => console.log(err))
    }
    getUsers()
  }, [])

  return (
    <div>
{ users?.length?     <table style={{ textAlign: 'left' }}>
        <tbody>
        <tr>
          <th>Username</th>
          <th>Email</th>
        </tr>
        {users.map(ele => (
          <tr key={ele.email}>
            <td>{ele.username}</td>
            <td>{ele.email}</td>
          </tr>
        ))}
        </tbody>
      </table>:<h1>Loading . . . .</h1>}
    </div>
  )
}
