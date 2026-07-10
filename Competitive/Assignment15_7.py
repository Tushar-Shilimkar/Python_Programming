# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

long_strings = lambda words: list(filter(lambda w: len(w) > 5, words))

strings = ["cat", "elephant", "dog", "giraffe", "ant", "crocodile"]
print(f"Strings with length > 5: {long_strings(strings)}")