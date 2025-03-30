import React from 'react';
import styles from './MainPage.module.css';

const MainPage = () => {
  return (
    <div className={styles.gridContainer}>
      {/* Container 1: Movie List */}
      <div className={styles.container}>
        <h1 className={styles.header}>Movie List</h1>
        <div className={styles.content}>Movie list content here</div>
      </div>

      {/* Container 2: Metadata Editor */}
      <div className={styles.container}>
        <h2 className={styles.header}>Metadata Editor</h2>
        <div className={styles.content}>Metadata Form</div>
      </div>

      {/* Container 3: Actors */}
      <div className={styles.container}>
        <h3 className={styles.header}>Actors</h3>
        <ul className={styles.list}>
          <li>Actor Selector</li>
          
        </ul>
      </div>

      {/* Container 4: Categories */}
      <div className={styles.container}>
        <h3 className={styles.header}>Categories</h3>
        <ul className={styles.list}>
          <li>Category Selector</li>
        </ul>
      </div>
    </div>
  );
};

export default MainPage;