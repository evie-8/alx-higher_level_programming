#!/usr/bin/node
const fun = 'C is fun';
const count = parseInt(process.argv[2]);
let i = 0;
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  while (i < count) {
    console.log(fun);
    i++;
  }
}
