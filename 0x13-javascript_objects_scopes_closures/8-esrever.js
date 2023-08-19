#!/usr/bin/node
exports.esrever = function (list) {
  let count = 0;
  const newList = [];
  for (count = list.length - 1; count >= 0; count--) {
    newList[list.length - count - 1] = list[count];
  }
  return newList;
};
