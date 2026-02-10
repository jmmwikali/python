# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def simple_interest(p, r, t):
    si = p * r * t / 100
    print(f"The Simple Interest is: {si}")

simple_interest(4500, 7, 8)

print("================================")

for numbers in range(2):
    simple_interest(50000, 5, 2)