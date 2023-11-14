#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  // Convert arguments to integers and filter out non-numeric values
  const numbers = args.map(Number).filter(value => !isNaN(value));

  // Sort the numbers in descending order
  const sortedNumbers = numbers.sort((a, b) => b - a);

  // Print the second largest number
  console.log(sortedNumbers[1]);
}
