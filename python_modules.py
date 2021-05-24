# What are Python Modules?
# We have built in Modules that we can find on Python's library
# If the value is 1.49 floor() 1, ceil()1.52 2
# We have a keyword called import that we can use to call a Module

# from random import random
# import math
# # If the user input is >= .50 apply ceil
# # If the user input is <= .49 apply floor
# number = random()
# print(number)
# if number >= 0.50:
#     print(math.ceil(number))
# else:
#     print(math.floor(number))

# print(random())
# num1 = 23.66
# print(num1)
# print(math.ceil(num1))
# print(math.floor(num1))
# What is the use case

# What is the use case
# os is used to get information about your localhost / your machine such as name, path etc
# Using a comma, we can use more than one Module on one line
import math
import os, sys, datetime

# Check how many CPUs I have
print(os.cpu_count())

# Check the date and time of today
print(datetime.datetime.today())

# % ? provides the remainder value left over
print(math.remainder(1, 5))

# Print out pi
print(math.pi)

working_dir = os.getcwd()
print("This is your current working directory " + working_dir)

system_path = sys.path
print("This is the path " + str(system_path))

def current_system_path():
    print("This is your current path ")
    return sys.path
print(current_system_path())

def current_working_directory():
    print("This is your current working directory ")
    return os.getcwd()
print(current_working_directory())

