#!/usr/bin/node
// class Rectangle that defines a triangle, creates an empty class if w or h <= 0

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
