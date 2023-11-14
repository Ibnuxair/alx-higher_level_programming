#!/usr/bin/node

// Accessing command line arguments using process.argv
const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

// Printing the two arguments in the specified format
console.log(`${arg1} is ${arg2}`);
