#!/usr/bin/node
const args = process.argv[2];
const value = args !== undefined ? args : 'No argument';
console.log(value);
