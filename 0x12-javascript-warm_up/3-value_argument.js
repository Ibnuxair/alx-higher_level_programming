#!/usr/bin/node

// Accessing command line arguments using process.argv
const args = process.argv.slice(2);
const firstArg = args[0];

// Printing the first argument or "No argument" if none is provided
console.log(firstArg !== undefined ? firstArg : "No argument");
