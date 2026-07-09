# Write a lambda function which accepts two numbers and returns minimum number.

minimum = lambda a, b: a if a < b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Minimum: {minimum(num1, num2)}")