#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nbr = number
print(f"Last digit of {number}", end=" ")
if nbr < 0:
    number = number * -1
last_dg = number % 10
if nbr < 0:
    last_dg = last_dg * -1
print(f"is {last_dg}", end=" ")
if last_dg > 5:
    print("and is greater than 5")
elif last_dg < 6 and last_dg != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
