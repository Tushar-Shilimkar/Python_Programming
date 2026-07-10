# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

odd_numbers = lambda nums: list(filter(lambda x: x % 2 != 0, nums))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Odd numbers: {odd_numbers(numbers)}")