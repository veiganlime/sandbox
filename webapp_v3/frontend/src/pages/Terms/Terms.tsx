import React from 'react';
import styles from './Terms.module.css';

const Terms = () => {
  return (
    <div className={styles.container}>
      <h1>Terms of Service</h1>
      <div className={styles.content}>
        <section>
          <h2>1. General Terms</h2>
          <p>By accessing our services, you agree to these terms.</p>
        </section>
        <section>
          <h2>2. Data Usage</h2>
          <p>Your data will be handled according to our privacy policy.</p>
        </section>
        <section>
          <h2>3. Service Limitations</h2>
          <p>We reserve the right to modify or discontinue services.</p>
        </section>
      </div>
    </div>
  );
};

export default Terms;