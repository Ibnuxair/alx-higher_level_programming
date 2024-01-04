#!/usr/bin/node

// Import the request module
const request = require('request');

// The id and the api url
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Making a GET request to fetch movie details
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Function to fetch character details and print their names
  const fetchAndPrintCharacterNames = async () => {
    for (const characterUrl of characters) {
      try {
        const characterResponse = await fetchCharacterDetails(characterUrl);
        const character = JSON.parse(characterResponse.body);
        console.log(character.name);
      } catch (error) {
        console.error('Error fetching character:', error);
      }
    }
  };

  // Function to fetch character details asynchronously
  const fetchCharacterDetails = (url) => {
    return new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(new Error(`Invalid status code: ${response.statusCode}`));
        } else {
          resolve({ response, body });
        }
      });
    });
  };

  // Call the function to fetch and print character names
  fetchAndPrintCharacterNames();
});
