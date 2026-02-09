# Create a List of Colors Blue, Green, Red, Pink , Black- Using a for Loop, Loop through the Colors

Colors = ["Blue", "Green", "Red", "Pink" , "Black"]
for list in Colors:
    print(list)

print("=====================================================")

# Research on python functions. Both with parameters and without parameters

# Function without parameters - they do a task without needing any input
def greet():
    print("Hello")

greet()

# Function with parameters - they recieve input and change behaviour based on it.
def greeting(name):
    print("Hello", name)

greeting("Jessica")

def add(x, y):
    print(x + y)

add(5,10)

def multiply(a, b):
    print(a * b)

multiply(6, 5)
