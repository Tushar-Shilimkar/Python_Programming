# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

is_odd = lambda n: n % 2 != 0

num = int(input("Enter a number: "))
print(f"Is odd: {is_odd(num)}")