import React from 'react';
import styles from './Container.module.css';

interface Props {
  children: React.ReactNode;
}

const Container = ({ children }: Props) => {
  return <main className={styles.container}>{children}</main>;
};

export default Container;