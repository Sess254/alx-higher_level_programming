#!/usr/bin/node
// script that prints My number: <first argument converted in integer>

const firstArgument = process.argv[2];

const intValue = parseInt(firstArgument);

if (!isNaN(intValue)) {
  console.log('My number:', intValue);
} else {
  console.log('Not a number');
}
