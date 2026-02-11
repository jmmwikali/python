# Question 5: Dictionary
shopping = {
    'sugar': 120,
    'rice': 200,
    'milk': 60,
    'bread': 60
}
print(f"This are the items in the list: {shopping}")


print("================================")
# 2. Find the sum of all items in above dictionary.
total = 0
for i in shopping.values():
    total = i + total
print(f"This is the total cost for all the items: {total}")


print("================================")
#  Create a List of town and reverse it.
towns = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"]
towns.reverse()
print(f"This is the reverse of the list: {towns}")


print("================================")
# Create a Loop to Print from 10 to 40
for number in range(10, 41):
    print(number)


print("================================")
# Create a Loop to Print from -10 to -50
for num in range(-10, -51, -1):
    print(num)


print("================================")
# Create a Function to Check if Year is Leap or Not
def check_year():
    year = int(input("Enter a year: "))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

check_year()