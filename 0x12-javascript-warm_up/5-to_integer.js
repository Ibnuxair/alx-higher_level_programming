#!/usr/bin/node

// Accessing command line arguments using process.argv
const args = process.argv.slice(2);
const firstArg = args[0];

// Converting the first argument to an integer
const num = parseInt(firstArg);

// Checking if the conversion was successful
if (!isNaN(num)) {
    // Printing the converted integer
    console.log(`My number: ${num}`);
} else {
    // Printing "Not a number" if conversion failed
    console.log("Not a number");
}
