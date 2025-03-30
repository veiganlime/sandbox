import React from 'react';
import styles from './Contact.module.css';

const Contact = () => {
  return (
    <div className={styles.container}>
      <h1>Contact Us</h1>
      <div className={styles.contactGrid}>
        <section className={styles.contactForm}>
          <h2>Send us a message</h2>
          <form>
            <input type="text" placeholder="Your Name" />
            <input type="email" placeholder="Your Email" />
            <textarea placeholder="Your Message"></textarea>
            <button type="submit">Send Message</button>
          </form>
        </section>
        <section className={styles.contactInfo}>
          <h2>Our Information</h2>
          <p>Email: info@Dataentity.com</p>
          <p>Phone: (123) 456-7890</p>
          <p>Address: 123 Data Street, Tech City</p>
        </section>
      </div>
    </div>
  );
};

export default Contact;