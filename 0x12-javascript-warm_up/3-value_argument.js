#!/usr/bin/node
// Script that prints the first argument passed to it

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.arg[2]);
