#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, function (err, response, body) {
  console.log('code: ' + response.statusCode);
  if (err) {}
});
