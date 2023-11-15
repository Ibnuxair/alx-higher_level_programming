#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
    constructor(size) {
	super(size, size); // Call the Rectangle constructor with size for both width and height
    }
}

module.exports = Square;
