#!/usr/bin/node
let fun = '';
const count = parseInt(process.argv[2]);
let i = 0;
let j = 0;
if (process.argv.length === 2 || isNaN(count)) {
  console.log('Missing size');
} else {
  while (i < count) {
    fun = fun + 'X';
    i++;
  }
  while (j < count) {
    console.log(fun);
    j++;
  }
}
