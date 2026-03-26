"""
DocStrings:
Lista (Cont.)
"""

"""List comprehensions"""
squares = [x**2 for x in range(1, 11)]
print(squares)

"""Slicing a list"""
finishers = ["sam", "bob", "ada", "bea"]
fisrst_two = finishers[:2]
print(finishers)
print(fisrst_two)

"""A different style"""
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item)

"""But clean"""
mylista = [1, 2]
for i in mylista:
    print(i)
