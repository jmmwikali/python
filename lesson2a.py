# Python Lists
# A List in Python is a collection of items that are ordered in a certain way
# A list is introduced by the use of the square brackets [].
# The items of a list are stored inside of indexes. Note: In programming we start counting from index zero (0).
# A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "Mclarel", "Range"]
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car in index four is:", cars[4])

# List slicing - this is creating a list from a given bigger list.
print(cars[4:])

# Printing from index zero to index three
print(cars[:4])

# Printing from Hiance to Probox
print(cars[2:5])

# List  - Mutability
# We use the function append to add an item to the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# We use the pop function to remove the last item in the list
cars.pop()
print(cars)

# We can use an index to add itms to a list
cars[5] = "Pajero"
print(cars)


# We use the sort function to sort out the items in alphabetical order
cars.sort()
print(cars)