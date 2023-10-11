#!/usr/bin/node

const fileSystem = require('fs');

try {
  fileSystem.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
} catch (err) {
  console.log(err);
}
