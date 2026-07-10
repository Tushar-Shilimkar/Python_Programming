# Write a lambda function which accepts two numbers and returns addition.

add = lambda a, b: a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Addition: {add(num1, num2)}")