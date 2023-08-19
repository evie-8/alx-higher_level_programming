#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let fun = '';
    let i = 0;
    let j = 0;
    for (i = 0; i < this.width; i++) {
      fun = fun + 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(fun);
    }
  }

  rotate () {
    const newHeight = this.width;
    this.width = this.height;
    this.height = newHeight;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
