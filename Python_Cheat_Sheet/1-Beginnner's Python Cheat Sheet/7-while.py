"""
DocStrigs: While Loops
A while loop repeats a block of code as longs as a certain condition is true.
While loops are especially useful when you can't know ahead of time how many times
as loop shouls run.
"""

"""As simples while loop"""
current_values = 1
while current_values <= 5:
    print(current_values)
    current_values += 1

"""An even simpler while loop"""
x = 0
while x < 5:
    print(x)
    x += 1  # Shorthand for x = x + 1


"""Letting the user choose when to quit"""

msg = ""
while msg != "quit":
    msg = input("What's your message? ")
    if msg != "quit":
        print(msg)
