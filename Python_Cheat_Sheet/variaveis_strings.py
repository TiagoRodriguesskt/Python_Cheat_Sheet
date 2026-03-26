"""
DocStrings:
Variables and Strings --> Variables are used to assign labels to values.
A string is a series of characters, surrounded by single or double quotes.
Python's f-strinngs allow you to ise variables inside strings to build
dynamic messages.
"""

"""Helo World"""
print("Hello World!")

"""Hello World with variable"""
msg = "Hello World!"
print(msg)

"""f-strings (using variable in strings)"""
first_name = "Albert"
last_name = "Einstein"
full_name = f"{first_name} {last_name}"
print(full_name)
