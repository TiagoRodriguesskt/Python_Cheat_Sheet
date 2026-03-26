"""
DocStrings: --> A list stores a series of items in a particular order.
You access items using an index, or within a loop.
"""

"""Make a list"""
bikes = ["trek", "redline", "giant"]

"""Get the first item in a list"""
first_bike = bikes[0]
print(first_bike)

"""Get the last item in a list"""
last_bike = bikes[-1]
print(last_bike)

"""Looping througn a list"""
for bike in bikes:
    print(bike)

"""Adding items to a list"""
bikes = []
bikes.append("trek")
bikes.append("redline")
bikes.append("giant")
print(bikes)

"""Making numerical list
Generate a list of numbers raised to the power of squares.
"""
squares = []
for x in range(1, 11):
    squares.append(x**2)
print(squares)
