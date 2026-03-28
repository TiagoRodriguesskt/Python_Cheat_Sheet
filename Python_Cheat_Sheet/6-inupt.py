"""
DocStrings:
User input --> Your programs can request user input.
All input can be stored as strings or numbers; you just need to define them.
"""

import math

"""Prompt for a value"""
name = input("What's your name? ")
print(f"Welcome {name}!")

"""Prompting for numerical input"""
age = int(input("How old are you? "))
print(f"Your age is {age}")

"""Float numbers"""
print("This is the value of pi.")
pi = float(math.pi)
print(pi)
