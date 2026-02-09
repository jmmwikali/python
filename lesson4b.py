# Loops - Sometimes we may need to do a piece of work a number of time repeatedly, and in such cases, we may use loops
# A loop is a control stucture that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python i.e The for loop and the while loop  

# Below is the syntax of a for loop in python
"""
for variable in range(n):
    # block of code to be executed
"""



for greating in range(5):
    print("Hello", greating)

print(".............................")

for number in range(10, 21):
    print(number)

print(".............................")
# Find the even numbers in the range of 50 to 71

for number in range(50, 71, 2):
    print(number)

print(".............................")
# Create a python program that prints the odd numbers from 100 to 150

for number in range(100, 150):
     if number % 2 != 0: 
         print(number)

print(".............................")
# Create a python program that prints the multiples of 3 starting from 201 to 150

for number in range(201, 150, -1): 
    if number % 3 == 0:
        print(number)

print(".............................")
# Create a python program that prints the leap years in between 2000 and 2024

for year in range(2000, 2024):
    if year % 400 == 0:
        print(year)