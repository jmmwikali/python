# Tuple
# It is an imutable type of  list (It cannot be changed)
# To introduce a tuple, we use parenthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# Slicing of a tuple
print(counties[3:])

# Accessing itesms of a tuple by use of the indexes
print(counties[4])

# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)