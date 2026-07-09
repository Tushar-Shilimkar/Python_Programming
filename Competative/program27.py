# Write a lambda function which accepts one number and returns cube of that number.

cube = lambda x: x ** 3

num = int(input("Enter a number: "))
print(f"Cube: {cube(num)}")