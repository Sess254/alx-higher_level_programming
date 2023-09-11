#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);

  const integers = numbers.filter(Number.isInteger);

  const sortedIntegers = integers.sort((a, b) => b - a);

  const secondBiggest = sortedIntegers[1];

  console.log(secondBiggest);
}
