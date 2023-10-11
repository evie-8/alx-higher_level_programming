#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, result, body) {
  if (err) {
    console.log(err);
  } else {
    const dicts = JSON.parse(body).reduce((acc, elem) => {
      if (!acc[elem.userId]) {
        if (elem.completed) {
          acc[elem.userId] = 1;
        }
      } else {
        if (elem.completed) {
          acc[elem.userId] += 1;
        }
      }
      return acc;
    }, {});
    console.log(dicts);
  }
});
