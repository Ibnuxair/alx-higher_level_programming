#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }

  n = parseInt(n);

  if (n < 0) {
    return "NaN";
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const args = process.argv.slice(2);
const num = args[0];

console.log(factorial(num));
