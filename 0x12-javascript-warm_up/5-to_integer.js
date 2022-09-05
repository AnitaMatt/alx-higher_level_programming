#!/usr/bin/node
const args = Math.floor(process.argv[2]);
if (parseInt(args)) {
  console.log(`My number: ${args}`);
} else {
  console.log('Not a number');
}
