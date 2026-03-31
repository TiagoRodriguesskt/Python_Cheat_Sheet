"""
DocStrings:
If statements --> Is statements are used to test for particular conditioms and
respond appropriately.
"""

"""Conditional test
equal           x = 10
not equal       x != 10
greater than    x > 10
or equal to     x >= 10
less than       x < 10
or equal to     x <= 10
"""

"""Conditional tests with lists
'trek' in bike
'surly' not in bike
"""
"""Assigning boolean values"""
game_active = True  # The letter T, always capitalized.
can_edit = False  # The letter F, always capitalized.
print(game_active, can_edit)

"""A simple if test"""
age = 18
if age >= 18:
    print("You can vote!")


"""if-elif-els statements"""
old = 15

if old < 4:
    ticket_price = 0
elif old >= 4 and old < 18:  # Se for entre 4 e 17 anos
    ticket_price = 10
elif old >= 18 and old < 65:  # Se for entre 18 e 64 anos
    ticket_price = 40
else:  # 65 anos ou mais
    ticket_price = 15

print(ticket_price)

"""Bigger number"""
num = 9
if num > 10:
    print("Number is greater than 10!")  # Number is greater than 10!
else:
    print("Number is not greter than 10")  # Number is not greter than 10
