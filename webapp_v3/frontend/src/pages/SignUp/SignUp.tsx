import React from 'react';
import styles from './SignUp.module.css';

const SignUp = () => {
  return (
    <div className={styles.container}>
      <div className={styles.signupCard}>
        <h1>Create Your Account</h1>
        <form>
          <input type="text" placeholder="Full Name" required />
          <input type="email" placeholder="Email Address" required />
          <input type="password" placeholder="Password" required />
          <input type="password" placeholder="Confirm Password" required />
          <button type="submit">Sign Up</button>
        </form>
        <div className={styles.loginLink}>
          Already have an account? <a href="/login">Log in</a>
        </div>
      </div>
    </div>
  );
};

export default SignUp;