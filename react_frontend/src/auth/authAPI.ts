import axios from 'axios'
import { Auth } from './authModel'

const client = axios.create({
  baseURL: 'http://localhost:8000/',
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    
  },
  withCredentials: true
})


const auth = () => {
  return {
    async login(credential: Auth) {
      return await client.post('/login', credential)
    }
  }
}

const authAPI = auth()

export { authAPI }
export default client
