#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let l = 'X';
    if (c !== undefined) {
      l = 'C';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(l.repeat(this.width));
    }
  }
}
module.exports = Square;
