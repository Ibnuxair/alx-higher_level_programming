#!/usr/bin/node

// Import file system
const fs = require('fs');

const file = process.argv[2];

// Read from the file
fs.readFile(file, 'utf-8', (err, data) => {
  // Check if there was an error
  if (err) {
    console.error(err);
    return;
  }
  // If there's no error
  console.log(data);
});
