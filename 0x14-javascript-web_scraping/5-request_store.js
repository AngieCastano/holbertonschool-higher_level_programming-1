#!/usr/bin/node

const URL = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request(URL, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const webContent = response.body;
    fs.writeFile(filePath, webContent, function (err) {
      if (err) {
        console.log(err);
      }
    }
    );
  }
});
