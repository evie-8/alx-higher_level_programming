#!/usr/bin/node
const a = parseInt(process.argv[2]);
if (process.argv.length === 2) {
  console.log(parseInt('1'));
} else {
  function factorial (a) {
    if (a === 1) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
  console.log(factorial(a));
}
