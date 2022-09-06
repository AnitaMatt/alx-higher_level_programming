#!/usr/bin/node
const args = process.argv;
let largest = parseInt(args[2]);
if (args.length < 4) {
  console.log(0);
} else {
  let second = largest;
  for (let i = 2; i < args.length; i++) {
    if (args[i] > largest) {
      second = largest;
      largest = parseInt(args[i]);
    } else {
      if (second > parseInt(args[i]) && second < largest) {
        continue;
      }
      second = parseInt(args[i]);
    }
  }
  console.log(second);
}
