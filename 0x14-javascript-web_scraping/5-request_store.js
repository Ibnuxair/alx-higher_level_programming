#!/usr/bin/node

// Required modules
const request = require('request');
const fs = require('fs');

// Extract URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the provided URL
request.get(url, (error, response, body) => {
  if (error) {
    // If there's an error during the request, log and exit
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    // If the response status code is not 200 (OK), log and exit
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  // Write the fetched content to the specified file path
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      // If there's an error while writing the file, log the error
      console.error('Error writing file:', err);
    }
  });
});
