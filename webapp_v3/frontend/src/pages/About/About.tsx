import React from 'react';
import styles from './About.module.css';

const About = () => {
  return (
    <div className={styles.container}>
      <h1>About Us</h1>
      <p>Welcome to Dataentity - your data management solution.</p>
      <div className={styles.content}>
        <section>
          <h2>Our Mission</h2>
          <p>To provide innovative data solutions that empower businesses.</p>
        </section>
        <section>
          <h2>Our Team</h2>
          <p>Experienced professionals dedicated to your data needs.</p>
        </section>
      </div>
    </div>
  );
};

export default About;