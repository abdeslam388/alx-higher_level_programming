#!/usr/bin/node

exports.esrever = function (list) {
  // Create a new array to store the reversed elements
  const reversed = [];

  // Iterate through the original list in reverse order and push elements to the new array
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }

  return reversed;
};

