import React from 'react';
import styles from './Dashboard.module.css';

const MainPage = () => {
  return (
    <div className={styles.pageLayout}>
      {/* Container 1: Portfolio Overview */}
      <div className={styles.container}>
        <h1 className={styles.header}>Portfolio Overview</h1>
        <div className={styles.content}>
          <p>Total invested: PLACEHOLDER</p>
          <p>The total holdings: PLACEHOLDER</p>
          <p>Unrealised Profit: PLACEHOLDER</p>
        </div>
      </div>

      {/* Container 2: Quantity*/}
      <div className={styles.container}>
        <h2 className={styles.header}>Quantity</h2>
        <div className={styles.content}>
          <p>Table content </p>
        </div>
      </div>

      {/* Container 3: Allocation */}
      <div className={styles.container}>
        <h3 className={styles.header}>Allocation</h3>
        <ul className={styles.list}>
        <p>Table content PLACEHOLDER</p>
        </ul>
      </div>

      {/* Container 4: Sector distribution */}
      <div className={styles.container}>
        <h3 className={styles.header}>Sector distribution</h3>
        <p>Table content PLACEHOLDER</p>
      </div>
    </div>
  );
};

export default MainPage;