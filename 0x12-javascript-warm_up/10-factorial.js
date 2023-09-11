#!/usr/bin/node
// Write a script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
