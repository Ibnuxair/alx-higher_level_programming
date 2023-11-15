#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
	if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
	    return {}; // Return an empty object if conditions aren't met
	} else {
	    this.width = w;
	    this.height = h;
	}
    }

    print() {
	if (!this.width || !this.height) {
	    console.log('Empty Object');
	} else {
	    for (let i = 0; i < this.height; i++) {
		console.log('X'.repeat(this.width));
	    }
	}
    }

    rotate() {
	[this.width, this.height] = [this.height, this.width];
    }

    double() {
	this.width *= 2;
	this.height *= 2;
    }
}

module.exports = Rectangle;
