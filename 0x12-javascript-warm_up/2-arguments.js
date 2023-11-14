#!/usr/bin/node

// Accessing command line arguments using process.argv
const args = process.argv.slice(2);
const numArgs = args.length;

// Printing a message based on the number of arguments
if (numArgs === 0) {
  console.log("No argument");
} else if (numArgs === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
