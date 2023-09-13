#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = list.map((_, index, arr) => arr[arr.length - 1 - index]);
  return reverseList;
};
