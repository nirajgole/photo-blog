import React from 'react'
import { BrowserRouter as Router, Route, Routes,Link } from 'react-router-dom'
import NotFound from './pages/NotFound'
import HomeView from './home/HomeView'
import LoginView from './user/LoginView'

export default function AppRouter() {
  return (
    <Router>
        <nav>
          <ul>
            <li>
              <Link to='/'>Home</Link>
            </li>
            <li>
              <Link to='login'>Login</Link>
            </li>
          </ul>
        </nav>
      <Routes>
        <Route path='/' element={<HomeView />} />
        <Route path='login' element={<LoginView />} />
        {/* <Route path="/recovery-password" element={<RecoveryPassword/>}/> */}
        <Route path='*' element={<NotFound />} />
      </Routes>
    </Router>
  )
}
