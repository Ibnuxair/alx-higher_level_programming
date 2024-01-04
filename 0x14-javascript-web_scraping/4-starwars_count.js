#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];
// The id
const characterId = '18';

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

  const films = JSON.parse(body).results;

  // Count the number of films where Wedge Antilles appears
  const numberOfFilms = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;

  console.log(numberOfFilms);
});
