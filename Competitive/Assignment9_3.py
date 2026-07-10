#  Write a program which accepts one number and prints square of that number.

def square(No):
    return No * No

num = int(input("Enter a number: "))
result = square(num)
print(f"Square of {num} is {result}")  