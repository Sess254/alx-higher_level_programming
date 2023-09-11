#!/usr/bin/node
// script that prints the first argument passed to it

if (process.argv[2]) {
  const firstArgument = process.argv[2];
  console.log(firstArgument);
} else {
  console.log('No argument');
}
