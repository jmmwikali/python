# Write a function that: Accepts a number n. Uses a for loop. Calculates the sum of numbers from 1 to n 

def number(n):
    total = 0    
    for number in range(1, (n + 1)):
        total += number
    print(f"The sum of all the numbers in the range is: {total}")

number(5)

print("=========================================")
# Write a function that: Accepts a number (Use input() function). Uses a while loop. Calculates the square of numbers from 1 up to that number
num = int(input("Enter a number: "))
def square(num):
    total = 1
    while total <= num:
        square = total ** 2
        print(f"The square of {total} is {square}")
        total += 1


square(num)