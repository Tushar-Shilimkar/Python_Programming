# Write a lambda function which accepts one number and returns True if divisible by 5.

is_divisible_by_5 = lambda n: n % 5 == 0

num = int(input("Enter a number: "))
print(f"Is divisible by 5: {is_divisible_by_5(num)}")