# Python While loop
# While loop executes a block of code repeatedly as long as a certain condition is true.

"""
Initializing a variable
while keyword,
followed by the condition/statement to be evaluated,
followed by a full colon (:)
code to be printed out,
increment/decrement
"""

number = 0
while number < 5:
    print("Hello Moses", number)
    number += 1

print("...............................................")
# Create a python program that prints the even numbers from 50 to 70

number = 50
while number <= 70:
    if number % 2 == 0:
        print(number)
    number += 1

print("...............................................")
# Below is a decrement example that prints the multiples of 3 starting from 201 to 150

number = 201
while number >= 150:
    if number % 3 == 0:
        print(number)
    number -= 1


# Research on python functions. Both with parameters and without parameters