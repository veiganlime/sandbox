import React, { useState } from 'react';
import { useNavigation } from '../../context/NavigationContext';
import styles from './Sidebar.module.css';

const Sidebar = () => {
  const [isVisible, setIsVisible] = useState(true);
  const { currentPage, setCurrentPage } = useNavigation();

  // Add/remove collapsed class to content area
  React.useEffect(() => {
    const content = document.querySelector(`.${styles.content}`);
    if (content) {
      if (!isVisible) {
        content.classList.add('collapsed');
      } else {
        content.classList.remove('collapsed');
      }
    }

    const navBrand = document.querySelector(`.${styles.navBrand}`);
    if (navBrand) {
      if (!isVisible) {
        navBrand.classList.add('collapsed');
      } else {
        navBrand.classList.remove('collapsed');
      }
    }
  }, [isVisible]);

  return (
    <>
      <button 
        className={`${styles.toggleButton} ${!isVisible && styles.hiddenButton}`}
        onClick={() => setIsVisible(!isVisible)}
        aria-label={isVisible ? 'Collapse sidebar' : 'Expand sidebar'}
      >
        {isVisible ? '◄' : '►'}
      </button>
      
      <aside className={`${styles.sidebar} ${!isVisible ? styles.hidden : ''}`}>
        <nav>
          <ul className={styles.navList}>
            <li 
              className={`${styles.navItem} ${currentPage === 'home' ? styles.active : ''}`}
              onClick={() => setCurrentPage('home')}
            >
              <span>🏠</span>
              <span>Home</span>
            </li>
            <li 
              className={`${styles.navItem} ${currentPage === 'dashboard' ? styles.active : ''}`}
              onClick={() => setCurrentPage('dashboard')}
            >
              <span>📊</span>
              <span>Dashboard</span>
            </li>
            <li 
              className={`${styles.navItem} ${currentPage === 'users' ? styles.active : ''}`}
              onClick={() => setCurrentPage('users')}
            >
              <span>👥</span>
              <span>Users</span>
            </li>
            <li 
              className={`${styles.navItem} ${currentPage === 'analytics' ? styles.active : ''}`}
              onClick={() => setCurrentPage('analytics')}
            >
              <span>📈</span>
              <span>Analytics</span>
            </li>
          </ul>
        </nav>
      </aside>
    </>
  );
};

export default Sidebar;