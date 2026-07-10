# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

minimum = lambda nums: reduce(lambda a, b: a if a < b else b, nums)

numbers = [3, 7, 2, 9, 4]
print(f"Minimum: {minimum(numbers)}")