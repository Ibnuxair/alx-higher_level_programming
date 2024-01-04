#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Send a GET request to the Star Wars API films endpoint
request.get(apiUrl, (error, response, body) => {
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
  const films = JSON.parse(body);

  // Filter movies where character ID 18 (Wedge Antilles) is present
  const moviesWithWedgeAntilles = films.results.filter((movie) =>
    movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  // Display the number of movies where Wedge Antilles is present
  console.log(moviesWithWedgeAntilles.length);
});
