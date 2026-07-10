# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

squares = lambda nums: list(map(lambda x: x ** 2, nums))

numbers = [1, 2, 3, 4, 5]
print(f"Squares: {squares(numbers)}")