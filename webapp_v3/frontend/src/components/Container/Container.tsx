import React from 'react';
import styles from './Container.module.css';

interface Props {
  children: React.ReactNode;
  title?: string;
}

const Container = ({ children, title }: Props) => {
  return (
    <div className={styles.container}>
      {title && <h2 className={styles.title}>{title}</h2>}
      {children}
    </div>
  );
};

export default Container;