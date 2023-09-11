#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”

if (process.argv[2] && process.argv[3]) {
  const firstArgument = process.argv[2];
  const secondArgument = process.argv[3];
  console.log(firstArgument, 'is', secondArgument);
} else {
  const firstArgument = process.argv[2] || 'undefined';
  const secondArgument = process.argv[3] || 'undefined';
  console.log(firstArgument, 'is', secondArgument);
}
