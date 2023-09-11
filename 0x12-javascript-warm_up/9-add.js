#!/usr/bin/node
// Write a script that prints the addition of 2 integers
// The first argument is the first integer
// The second argument is the second integer

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (!isNaN(num1) && !isNaN(num2)) {
  const result = num1 + num2;
  console.log(result);
} else {
  console.log('NaN');
}
