#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb = abs(number) % 10
if number < 0:
    numb = -numb
if numb == 0:
    print(f"Last digit of {number:d} is {numb:d} and is 0")
elif numb > 5:
    print(f"Last digit of {number:d} is {numb:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {numb:d} and is less than 6 and not 0")
