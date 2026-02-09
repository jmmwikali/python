# For loop can also be used to iterate through a list, turple, string or even a dictionary.

name = "Jessica"

for letter in name:
    if letter == "s":
        print("s -This is letter s")
    else:
        print(letter)

print(".........................................")
# Below is a list of counties

counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]
print(counties)

for county in counties:
    print(county)

print(".........................................")
search = input("Enter a county to search: ")

found = False
for county in counties:
    if county == search:
        found = True
        break  # stop checking once found

if found:
    print(search, "is available")
else:
    print(search, "is not available.")

print(".........................................")
# For loop can also be used to iterate through a dictionary.

player = {
    "name": "Mbappe",
    "age": 25,
    "teams": ["PSG", "Manoco", "France"],
    "nationality": "French"
}

for key in player.keys():
    print(key)

for value in player.values():
    print(value)
print("..........................................")
# Loop through the teams the player has played for
for teams in player["teams"]:
    print(teams)