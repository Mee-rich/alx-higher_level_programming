#!/usr/bin/node
// A class Rectangle that defines a rectangle

class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
			return ("Rectangle {}");
		}

		this.width = w;
		this.height = h;
	}

	print() {
		if (!this.width || !this.height) {
			console.log("Empty rectangle");
			return;
		}

		for (let i = 0; i < this.height; i++) {
			let row = "";
			for (let j = 0; j < this.width; j++) {
				row += "X";
			}
			console.log(row);
		}
	}
}

module.exports = Rectangle;
