# Write a lambda function which accepts one number and returns True if number is even otherwise False.

is_even = lambda n: n % 2 == 0

num = int(input("Enter a number: "))
print(f"Is even: {is_even(num)}")