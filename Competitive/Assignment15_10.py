# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

count_even = lambda nums: len(list(filter(lambda x: x % 2 == 0, nums)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Count of even numbers: {count_even(numbers)}")