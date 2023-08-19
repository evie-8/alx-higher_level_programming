#!/usr/bin/node
const list = require('./100-data').list;
const newList = [];
let i = 0;
for (i = 0; i < list.length; i++) {
  newList[i] = list[i] * i;
}
console.log(list);
console.log(newList);
