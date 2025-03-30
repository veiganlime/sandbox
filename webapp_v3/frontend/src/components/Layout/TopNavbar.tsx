import React from 'react';
import { useNavigation } from '../../context/NavigationContext';
import styles from './TopNavbar.module.css';

const TopNavbar = () => {
  const { setCurrentPage } = useNavigation();

  return (
    <nav className={styles.navbar}>
      <div className={styles.navBrand}>Dataentity</div>
      <div className={styles.navItems}>
        <a onClick={() => setCurrentPage('about')}>About Us</a>
        <a onClick={() => setCurrentPage('contact')}>Contact</a>
        <a onClick={() => setCurrentPage('terms')}>Terms</a>
        <a onClick={() => setCurrentPage('signup')} className={styles.signUp}>Sign Up</a>
      </div>
    </nav>
  );
};

export default TopNavbar;