#!/usr/bin/node
// script that concats 2 files
const fs = require('fs');
const a = fs.readFileSync(process.argv[2], 'utf-8');
const b = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], a + b);
