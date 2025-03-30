import { NavigationProvider, useNavigation } from './context/NavigationContext';
import Sidebar from './components/Layout/Sidebar';
import Dashboard from './pages/MainPage/Dashboard';
import Home from './pages/Home/Home';
import Users from './pages/Users/Users';
import Analytics from './pages/Analytics/Analytics';
import styles from './App.module.css';

function AppContent() {
  const { currentPage } = useNavigation();

  return (
    <div className={styles.appContainer}>
      <Sidebar />
      <div className={styles.content}>
        {currentPage === 'home' && <Home />}
        {currentPage === 'dashboard' && <Dashboard />}
        {currentPage === 'users' && <Users />}
        {currentPage === 'analytics' && <Analytics />}
      </div>
    </div>
  );
}

function App() {
  return (
    <NavigationProvider>
      <AppContent />
    </NavigationProvider>
  );
}

export default App;