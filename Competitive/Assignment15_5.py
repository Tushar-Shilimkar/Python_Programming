# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

maximum = lambda nums: reduce(lambda a, b: a if a > b else b, nums)

numbers = [3, 7, 2, 9, 4]
print(f"Maximum: {maximum(numbers)}")