#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = 'Last digit of'

digit = abs(number) % 10
if digit > 5:
    print(f"{str:s} {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"{str:s} {number:d} is {digit:d} and is 0")
else:
    print("and is less than 6 and not 0")
