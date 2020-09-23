#!/usr/bin/node
const fileName = process.argv[2];
const fs = require('fs');

fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
