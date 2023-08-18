#!/usr/bin/node
const convert = parseInt(process.argv[2]);

if (process.argv.length === 2) {
  console.log('Not a number');
} else {
  if (isNaN(convert)) {
    console.log('Not a number');
  } else {
    console.log('My number:', convert);
  }
}
