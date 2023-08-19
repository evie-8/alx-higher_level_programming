#!/usr/bin/node
const dicts = require('./101-data').dict;
const newDict = {};
for (const i in dicts) {
  const j = dicts[i];
  if (!(j in newDict)) {
    newDict[j] = [];
  }
  newDict[j].push(i);
}
console.log(newDict);
