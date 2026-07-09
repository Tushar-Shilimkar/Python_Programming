# Write a lambda function which accepts one number and returns square of that number.

square = lambda x: x ** 2

num = int(input("Enter a number: "))
print(f"Square: {square(num)}")