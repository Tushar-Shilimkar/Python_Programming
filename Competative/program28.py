# Write a lambda function which accepts two numbers and returns maximum number.

maximum = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Maximum: {maximum(num1, num2)}")