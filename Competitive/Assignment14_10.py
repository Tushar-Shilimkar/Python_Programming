# Write a lambda function which accepts three numbers and returns largest number.

largest = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(f"Largest: {largest(num1, num2, num3)}")