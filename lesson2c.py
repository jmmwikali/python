# A dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of curly braces {}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary, we use the keys.

phonebook = {
    "Benson" : "254757853901",
    "Mary" : "254720950017",
    "Stephen" : "254711074993"
    }

# Showing the entire dictionary
print(phonebook)
print(type(phonebook))

# Print out benson's number
print(phonebook["Benson"])

print(".........................................")

player = {
    "Name" : "Messi",
    "Age" : "40",
    "Teams" : ["PSG", "Barcelona", "Argentina"],
    "More" : {
        "Children" : 3,
        "Residence" : "US",
        "Phone" : (25478209734, 25478762198, 2547923749)
    }
}
print("One of the teams he played for:", player["Teams"][1])

# Research on if...else statements in python.

print("Messi's second number is:", player["More"]["Phone"][1])
