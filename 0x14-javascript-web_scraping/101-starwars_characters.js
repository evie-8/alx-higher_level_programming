#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function helperFunction (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).name);
    helperFunction(arr, i + 1);
  });
}

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const chars = JSON.parse(body).characters;
  helperFunctiont(chars, 0);
});
