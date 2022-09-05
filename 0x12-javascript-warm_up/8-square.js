#!/usr/bin/node
const args = Math.floor(parseInt(process.argv[2]));
if (!args) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args; i++) {
    let result = '';
    for (let j = 0; j < args; j++) {
      result += 'X';
    }
    console.log(result);
  }
}
