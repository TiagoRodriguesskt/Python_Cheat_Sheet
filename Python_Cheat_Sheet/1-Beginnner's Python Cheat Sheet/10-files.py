"""
DocStrings: --> Working with files
Your programs can read from  files write to files. The pathlib library makes it easier
to work with files and directories. Once you have a path defined, you can work with the
read_text() and write_read_text() methods.
"""

"""Reading the contents of a file.
The read_text() method reads in the entire contents of a file. You can then process 
each line as you need to.
"""

from pathlib import Path  # noqa: E402

patch = Path("Infinte.txt")
contents = patch.read_text()
lines = contents.splitlines()

for line in lines:
    print(line)

"""Writing to a file"""
path = Path("Infinte.txt")

msg = "I am reading this file."
patch.write_text(msg)

"""Exceptions
Exceptions help you respond appropriately to errors that are likely to occur. You 
place code that might cause an error in the 'try block'. Code that should run in 
response to an error goes in the except block. Code that should run only if the try 
block was successful goes in the else block.
"""
"""Catching an exception"""
prompt = "How many tickets do you need? "
num_tickets = input(prompt)

try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")

"""Zen of Python
Simples is better than complex.
If you haves a choice between a simple and a complex solution, and both work, use 
the semples solution. Your code will be easier to maintain, and it will be easier
for you and others to build on that code later on.
"""
