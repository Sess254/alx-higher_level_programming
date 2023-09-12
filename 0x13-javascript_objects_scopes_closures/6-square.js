#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
