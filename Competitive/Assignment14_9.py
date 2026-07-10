# Write a lambda function which accepts two numbers and returns multiplication.

multiply = lambda a, b: a * b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Multiplication: {multiply(num1, num2)}")