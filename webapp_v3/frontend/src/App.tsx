import { NavigationProvider, useNavigation } from './context/NavigationContext';
import Sidebar from './components/Layout/Sidebar';
import TopNavbar from './components/Layout/TopNavbar';
import Dashboard from './pages/Dashboard/Dashboard';
import Home from './pages/Home/Home';
import Users from './pages/Users/Users';
import Analytics from './pages/Analytics/Analytics';
import About from './pages/About/About';
import Contact from './pages/Contact/Contact';
import Terms from './pages/Terms/Terms';
import SignUp from './pages/SignUp/SignUp';
import styles from './App.module.css';

function AppContent() {
  const { currentPage } = useNavigation();

  return (
    <div className={styles.appContainer}>
      <TopNavbar />
      <div className={styles.mainContent}>
        <Sidebar />
        <div className={styles.content}>
          {currentPage === 'home' && <Home />}
          {currentPage === 'dashboard' && <Dashboard />}
          {currentPage === 'users' && <Users />}
          {currentPage === 'analytics' && <Analytics />}
          {currentPage === 'about' && <About />}
          {currentPage === 'contact' && <Contact />}
          {currentPage === 'terms' && <Terms />}
          {currentPage === 'signup' && <SignUp />}
        </div>
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