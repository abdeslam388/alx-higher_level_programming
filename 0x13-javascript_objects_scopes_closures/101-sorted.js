#!/usr/bin/node

const data = require('./101-data');
const dict = data.dict;

const sortedDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }

  sortedDict[occurrence].push(userId);
}

console.log(sortedDict);

