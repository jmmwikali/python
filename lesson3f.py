# Create a python program that is able to determain whether a number entered is an odd number or an even number.

number = int(input("Enter number: "))

if number % 2 == 0:
    print("Number is an even number")
else:
    print("Number is an odd number")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is greater than 50kgs and age is above 18, they can be able to donate blood, else, not possible.

age = int(input("Enter age: "))
weight = float(input("Enter weight: "))

if age >= 18 and weight > 50:
    print("Can donate")
else:
    print("Not possible")