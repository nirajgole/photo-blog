import {  Route, Routes } from 'react-router-dom'
import NotFound from './pages/NotFound'
import HomeView from './home/HomeView'
import LoginView from './user/LoginView'
import ProtectedRoutes from './ProtectedRoutes'
import HeaderView from './header/HeaderView'
import Landing from './pages/Landing'

export default function AppRouter() {
  return (
    <>

      <Routes>
        <Route path='login' element={<LoginView />} />
        {/* <Route path="/recovery-password" element={<RecoveryPassword/>}/> */}
        <Route element={<ProtectedRoutes />}>
        <Route path='home' element={<HomeView />} />
        </Route>
        <Route path='/' element={<Landing />} />
        <Route path='*' element={<NotFound />} />
      </Routes>
    </>
  )
}
