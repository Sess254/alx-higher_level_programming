#!/usr/bin/python3

for l in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((l - (ord('a') - ord('A'))) if l % 2 else l), end='')
