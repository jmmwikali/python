# Generate a program that will store some Gross Salary in variable. Determine the monthly contribution someone will pay.(Use IF...ELIF...ELSE statement)

Gross_Income = int(input("Enter Gross Income(Ksh): "))

print("Your Gross Income is:", Gross_Income)

if Gross_Income > 0 and Gross_Income <= 5999:
    print("Monthly Contribution(Ksh) is: 150.00")
elif Gross_Income >= 6000 and Gross_Income <= 7999:
    print("Monthly Contribution(Ksh) is: 300.00")
elif Gross_Income >= 8000 and Gross_Income <= 11999:
    print("Monthly Contribution(Ksh) is: 400.00")
elif Gross_Income >= 12000 and Gross_Income <= 14999:
    print("Monthly Contribution(Ksh) is: 500.00")
elif Gross_Income >= 15000 and Gross_Income <= 19999:
    print("Monthly Contribution(Ksh) is: 600.00")
elif Gross_Income >= 20000 and Gross_Income <= 24999:
    print("Monthly Contribution(Ksh) is: 750.00")
elif Gross_Income >= 25000 and Gross_Income <= 29999:
    print("Monthly Contribution(Ksh) is: 850.00")
elif Gross_Income >= 30000 and Gross_Income <= 49999:
    print("Monthly Contribution(Ksh) is: 1,000.00")
elif Gross_Income >= 50000 and Gross_Income <= 99999:
    print("Monthly Contribution(Ksh) is: 1,500.00")
else:
    print("Monthly Contribution(Ksh) is: 2,000.00")