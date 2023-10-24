#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(`Request failed with status code ${response ? response.statusCode : 'unknown'}`);
  } else {
    const todos = JSON.parse(body);

    const completedTasksByUser = todos.reduce((result, task) => {
      if (task.completed) {
        if (!result[task.userId]) {
          result[task.userId] = 1;
        } else {
          result[task.userId]++;
        }
      }
      return result;
    }, {});

    console.log(completedTasksByUser);
  }
});
