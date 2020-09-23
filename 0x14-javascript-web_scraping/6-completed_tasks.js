#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
const result = {};

request(URL, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    for (const i of tasks) {
      if (i.completed === true) {
        if (result[i.userId] === undefined) {
          result[i.userId] = 1;
        } else {
          result[i.userId] += 1;
        }
      }
    }
    console.log(result);
  }
});
