import { useLocation } from 'react-router'
import { Navigate, Outlet } from 'react-router-dom'
import { useAuth } from './App'


const ProtectedRoutes = () => {
  const { isLoggedIn } = useAuth()
  const location = useLocation()
  return isLoggedIn ? (
    <Outlet />
  ) : (
    <Navigate to='/' replace state={{ from: location }} />
  )
}

export default ProtectedRoutes
