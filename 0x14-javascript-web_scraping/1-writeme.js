#!/usr/bin/node

// Import file system
const fs = require('fs');

const file = process.argv[2];
const content = process.argv[3];

// Write the file
fs.writeFile(file, content, 'utf-8', (err) => {
  // Check if there was an error
  if (err) {
    console.error(err);
  }
});
