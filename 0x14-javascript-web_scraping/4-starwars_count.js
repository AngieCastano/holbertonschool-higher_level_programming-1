#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
const characterID = '18';
const characterURL = 'https://swapi-api.hbtn.io/api/people/' + characterID + '/';
let counter = 0;

request(URL, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const jsonObj = JSON.parse(body);
    const movies = jsonObj.results;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      if (characters.includes(characterURL)) {
        counter += 1;
      }
    }
    console.log(counter);
  }
});
