import axios from 'axios'
import { Auth } from './authModel'

const client = axios.create({
  baseURL: 'http://localhost:8000/',
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': 'http://127.0.0.1:5173/',
  },
  withCredentials: true
})


const auth = () => {
  return {
    async login(credential: Auth) {
      console.log(credential)
      return await client.post('/login', credential)
    }
  }
}

const authAPI = auth()

export { authAPI }
export default client
