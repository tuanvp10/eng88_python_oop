# What are Python Modules?
# We have built in Modules that we can find on Python's library
# If the value is 1.49 floor() 1, ceil()1.52 2
# We have a keyword called import that we can use to call a Module

from random import random
import math
# If the user input is >= .50 apply ceil
# If the user input is <= .49 apply floor
number = random()
print(number)
if number >= 0.50:
    print(math.ceil(number))
else:
    print(math.floor(number))

# print(random())
# num1 = 23.66
# print(num1)
# print(math.ceil(num1))
# print(math.floor(num1))
# What is the use case
