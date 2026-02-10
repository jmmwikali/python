# Create a function that: Takes no parameters. Uses arithmetic operators to calculate the area of a rectangle. Prints the result 
def rectangle():
    length = 12
    width = 8
    area = length * width
    print(f"This is the area of the rectangle: {area}")

rectangle()

print("========================================")
# Create a function that: Accepts two numbers as parameters. Returns their sum, difference, product, and division 
def numbers(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    division = x / y
    print(f"The sum of the numbers is: {sum}")
    print(f"The differense of the numbers is: {difference}")
    print(f"The product of the numbers is: {product}")
    print(f"The quotient of the numbers is: {division}")

numbers(20, 8)

print("========================================")
# Write a function that: Accepts a number (use input function). Checks whether the number is: Positive, Negative, Zero 
number = int(input("Enter a number: "))
def check(number):
    if number > 0:
        print(f"{number} is a positive number")
    elif number < 0:
        print(f"{number} is a negative number")
    else:
        print(f"{number} is zero")
    
check(number)
