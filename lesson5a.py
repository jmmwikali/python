# Python Functions
# They are a block of code/statements that performs a given task/action. They can be reused throughout the program to perform different tasks.
# Functionsa are defined using the def keyword. (define)
# We have to main types of functions i.e 
# 1. In-built functions - They come pre-installed with the interpreter i.e print(), pop(), range(), input(), append()
# 2. User-defined functions - They are creasted by a programmer to solve a task.
# To define a function you need to give it a name followed by parenthesis.
# For the function, it is usually indented and to invoke a functionwe use the function name.

def greeting():
    print("Hello, how are you?")

# Below we call the function by use of its name
greeting()

print("=============================")

# Addition Function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is:", sum)

addition()

print("=============================")
# Create a function that is able to multipy three values
def multiply():
    num1 = 15
    num2 = 5
    num3 = 12
    product = num1 * num2 *num3
    print("The product of the numbers is:", product)

multiply()

print("=============================")
# Below is a division function
def divide():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    quotient = num1 / num2
    print("The answer is: ", quotient)
    print("-------")
    
# Adding a statements to identify each loop.
position = ["first", "second", "third"]  # list of names
for division, name in enumerate(position):
    print(f"This is the {name} calculation")
    divide()
    

    
