import React, { useState } from 'react';
import Display from './Display';
import ButtonGrid from './ButtonGrid';
import styles from './Calculator.module.css';

const Calculator = () => {
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');

  const handleButtonClick = (value) => {
    if (value === 'C') {
      setInput('');
      setResult('');
      return;
    }
    if (value === '=') {
      try {
        // eslint-disable-next-line no-eval
        const evalResult = eval(input);
        setResult(String(evalResult));
      } catch (e) {
        setResult('Error');
      }
      return;
    }
    setInput((prev) => prev + value);
  };

  return (
    <div className={styles.calculator}>
      <Display input={input} result={result} />
      <ButtonGrid onButtonClick={handleButtonClick} />
    </div>
  );
};

export default Calculator;
