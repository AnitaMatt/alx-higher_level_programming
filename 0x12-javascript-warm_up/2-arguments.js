#!/usr/bin/node
const numOfArgv = process.argv.length - 2;
if (numOfArgv === 0) {
  console.log('No argument found');
} else if (numOfArgv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
