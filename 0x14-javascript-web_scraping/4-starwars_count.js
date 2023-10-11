#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const numberCount = JSON.parse(body).results.filter((elem) => {
      return elem.characters.filter((url) => { return url.includes('18'); }).length;
    }).length;
    console.log(numberCount);
  }
});
