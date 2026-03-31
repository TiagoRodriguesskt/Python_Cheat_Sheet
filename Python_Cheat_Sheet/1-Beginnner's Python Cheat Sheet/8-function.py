"""
DocStrings: Functions
Functions are named blocks of code, designed to do one specific job.
Information passed to a function is called on argument, and information received
by a function is called a peramenter.
"""

"""A simples functions"""


def my_user():
    """Display a simples freeting."""
    print("Hello!")


my_user()

"""Passing an argument"""


def greet_user(username):
    """Display a personalized greeting"""
    print(f"Hello, {username}!")


greet_user("Tiago")

"""Defaut values for perameters"""


def make_pizza(toppin="pinaapple"):
    """Make a single-tooping pizza"""
    print(f"Have a {toppin} pizza!")


make_pizza()
make_pizza("mushroom")

"""Returning a value"""


def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y


sum = add_numbers(5, 3)
print(sum)


"""Return"""


def addd(x, y):
    print(f"x is {x}, y is {y}")
    return x + y


print(addd(5, 6))


"""Positional arguments"""


def varargs(*args):
    return args


print(varargs(1, 2, 3))

"""Keyword arguments"""


def keyword_args(**kwargs):
    return kwargs


# --> {"big": "foot", "loch": "ness"}
result = keyword_args(big="foot", loch="ness")
print(result)

# Input -->     print(keyword_args)
# Output --> #  <function keyword_args at 0x000001263B5880D0>


"""Returning multiple"""


def swap(x, y):
    return y, x


x = 1
y = 2
x, y = swap(x, y)

# => x = 2, y = 1
print(swap(x, y))


"""Defaut value"""


def add(x, y=10):
    return x + y


# If you want to get the result of x and y, you have to create a variable!
add(5)  # => 15
add(5, 20)  # => 25

print(add(x, y))

"""Anonymous functions"""
# You created a function that squares x and y and adds them. Passing 2 and 1,
# the calculation is (), resulting in 5

# => True
print((lambda x: x > 2)(3))

# => 5
print((lambda x, y: x**2 + y**2)(2, 1))
