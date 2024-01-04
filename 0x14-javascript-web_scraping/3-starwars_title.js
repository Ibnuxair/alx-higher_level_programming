#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from command line arguments
const movieID = process.argv[2];

// Create the URL for the specific movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Send a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  // Check for request errors
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the response status code is not 200 (OK)
  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  // Parse the JSON response body
  const movie = JSON.parse(body);

  // Display the movie title
  console.log(movie.title);
});
