#!/usr/bin/node
const squares = require('./5-square');
class Square extends squares {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let i = 0;
    let j = 0;
    let fun = '';
    for (i = 0; i < this.width; i++) {
      fun = fun + c;
    }
    for (j = 0; j < this.height; j++) {
      console.log(fun);
    }
  }
}
module.exports = Square;
