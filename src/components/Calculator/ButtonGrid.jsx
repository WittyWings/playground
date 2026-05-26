import React from 'react';
import styles from './ButtonGrid.module.css';

const buttons = [
  '7', '8', '9', '/',
  '4', '5', '6', '*',
  '1', '2', '3', '-',
  '0', ' , 'C', '+',
  '=',
];

const ButtonGrid = ({ onButtonClick }) => (
  <div className={styles.grid}>
    {['7','8','9','/','4','5','6','*','1','2','3','-','0','C','+','='].map((label) => (
      <button
        key={label}
        className={styles.button}
        onClick={() => onButtonClick(label)}
      >
        {label}
      </button>
    ))}
  </div>
);

export default ButtonGrid;
