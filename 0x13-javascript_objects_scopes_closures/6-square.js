#!/usr/bin/node
class Square extends require('./5-square.js') {

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += c;
      }
      console.log(result);
    }
  }
}
module.exports = Square
