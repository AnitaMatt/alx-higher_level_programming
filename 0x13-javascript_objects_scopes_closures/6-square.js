#!/usr/bin/node
class Square extends require('./5-square') {

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let result = '';
      for (let j = 0; j < this.size; j++) {
        result += c;
      }
      console.log(result);
    }
  }
}
module.exports = Square
