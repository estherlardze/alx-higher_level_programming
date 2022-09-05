#!/usr/bin/node
const myFunct = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
module.exports = {
  myFunct: myFunct
}
