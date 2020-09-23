#!/usr/bin/node
const fileName = process.argv[2];
const stringToWrite = process.argv[3];
const fs = require('fs');

fs.writeFile(fileName, stringToWrite, 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
