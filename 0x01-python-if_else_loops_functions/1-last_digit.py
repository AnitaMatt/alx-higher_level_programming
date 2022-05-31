#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = number
if new_number < 0:
    new_number = new_number * -1
l_digit = new_number % 10
if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit < 6 and l_digit != 0:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
