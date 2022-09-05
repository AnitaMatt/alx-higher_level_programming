#!/usr/bin/node
const args = process.argv;
let largest = parseInt(args[2]);
let second = largest;
if (args.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (args[i] > largest) {
      second = largest;
      largest = parseInt(args[i]);
    }
  }
  console.log(second);
}
