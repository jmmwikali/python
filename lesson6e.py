# On the try and except block: You run some codes/statements and if it is successful, the try block will get executed. Otherwise the except block will be executed when there is an anticipated error.
try:
    number = 100 
    answer = number / 0
    print("The answer is: ", answer)
except Exception as e:
    print(f"There is an error: {e}")

try:
    result = "5" + 3
    print(result) 
except Exception as n:
    print(f"There is an error: {n}")

try:
    num = int("Name") 
    print(num)
except Exception as x:
    print(f"There is an error: {x}")
