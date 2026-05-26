import React from 'react';
import styles from './Display.module.css';

const Display = ({ input, result }) => (
  <div className={styles.display}>
    <div className={styles.input}>{input}</div>
    <div className={styles.result}>{result}</div>
  </div>
);

export default Display;
