# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

divisible_by_3_and_5 = lambda nums: list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))

numbers = [10, 15, 20, 30, 45, 50, 60]
print(f"Divisible by both 3 and 5: {divisible_by_3_and_5(numbers)}")