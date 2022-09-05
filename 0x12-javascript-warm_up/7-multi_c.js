#!/usr/bin/node
const args = Math.floor(parseInt(process.argv[2]));
if (!args) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < args; i++) {
    console.log('C is fun');
  }
}
