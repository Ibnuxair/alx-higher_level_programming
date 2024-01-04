#!/usr/bin/node

// Import the request module
const request = require('request');

// The api url
const url = process.argv[2];

// Making a GET request to fetch todos data
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);

  // Initialize an object to store the count of completed tasks for each user
  const completedTasks = {};

  // Loop through each todo item
  for (const todo of todos) {
    // Check if the task is completed
    if (todo.completed) {
      // Increment the completed task count for the user ID
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  }

  // Format the output as per the expected format
  const formattedOutput = {};
  for (const key in completedTasks) {
    formattedOutput[key] = completedTasks[key];
  }

  console.log(formattedOutput);
});
