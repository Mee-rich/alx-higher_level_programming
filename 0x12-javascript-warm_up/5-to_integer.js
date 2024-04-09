#!/usr/bin/node
// Prints two arguments passed to it

const int = Math.floor(Number(process.argv[2]));
console.log(isNaN(int) ? 'Not a number' : `My number: ${int}`);
