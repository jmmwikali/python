# Functions wth parameters
# Parameters - They are values that get passed as arguments given to a function inside of the parenthesis.

def greeting(name):
    print(f"Hello {name}! How are you? Hope everythig is fine.")

greeting("Jessica")
greeting("Trevor")

print("=========================================")
def message(names):
    print(f"Hello {names}. We shall be having a general meeting on date....Please avail yourself.")

message("Johnson")
message("Mercy")

print("=========================================")
# Create a function that accepts parameters to add two numbers

def addition(x, y):
    sum = x + y
    print(f"The sum of the numbers is: {sum}")

addition(5, 10)
addition(78, 92)

