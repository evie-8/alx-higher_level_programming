#!/usr/bin/node
const is = ' is ';
let sentence;
if (process.argv.length === 2) {
  console.log('undefined is undefined');
} else if (process.argv.length === 3) {
  sentence = process.argv[2] + is + 'undefined';
  console.log(sentence);
} else if (process.argv.length === 4) {
  sentence = process.argv[2] + is + process.argv[3];
  console.log(sentence);
}
