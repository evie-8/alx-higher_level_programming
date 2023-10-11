#!/usr/bin/node

const fileSystem = require('fs');

fileSystem.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
