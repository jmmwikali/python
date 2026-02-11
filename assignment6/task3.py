# Create a Function to Find Body Mass Index
def BMI():
    w = float(input("Enter the weight: "))
    h = float(input("Enter the height: "))
    BMI = w / (h ** 2)
    print(f"The Body Mass Index is: {BMI}")

BMI()

print("==================================")
# Using if statements, write a Python program to check how much a traveler would pay based of distance.
distance = int(input("Enter the distance to be travelled: "))
if distance > 3 and distance <= 5:
    print(f"The cost is: Ksh 375")
elif distance > 5 and distance <= 10:
    print(f"The cost of the trip is: Ksh 750")
elif distance > 10 and distance <= 20:
    print(f"The cost of the trip is: Ksh 1,500")
elif distance > 20 and distance <= 50:
    print(f"The cost of the trip is: Ksh 3,750")
elif distance > 50 and distance <= 100:
    print(f"The cost of the trip is: Ksh 750")
else:
    print("Walking distance")

print("====================================")
# Create a Python Program to find if number is Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")