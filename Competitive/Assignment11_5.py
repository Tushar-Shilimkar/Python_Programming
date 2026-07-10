# Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

num = input("Enter a number: ")

reverse = num[::-1]

if num == reverse:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")