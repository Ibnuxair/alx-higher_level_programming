#!/usr/bin/node

// Import request
const request = require('request');

const url = process.argv[2];

// Check if the url is provided
if (!url) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

// Make the request and display the status
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
