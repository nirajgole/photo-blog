import { useState, createContext, useContext } from 'react'
import AppRouter from './routes'
import HeaderView from './header/HeaderView'

//creating custom use-context hook
const AuthContext = createContext({})

export const useAuth = () => useContext(AuthContext)

const AuthContextProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false)

  return (
    <AuthContext.Provider value={{ isLoggedIn, setIsLoggedIn }}>
      {children}
    </AuthContext.Provider>
  )
}

const App = () => {
  return (
    <AuthContextProvider>
      <div className='App'>
        <HeaderView />
        <div style={{ display: 'grid', placeItems: 'center', minHeight: '50vh' }}>
          <AppRouter />
        </div>
      </div>
    </AuthContextProvider>
  )
}

export default App
