# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

product = lambda nums: reduce(lambda a, b: a * b, nums)

numbers = [1, 2, 3, 4, 5]
print(f"Product: {product(numbers)}")