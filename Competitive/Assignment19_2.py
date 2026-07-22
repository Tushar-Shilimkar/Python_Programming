"""
    Write a program which contains one lambda function which accepts two parameters and return its multiplication.

    Input : 4 3 Output : 12
    Input : 6 3 Output : 18
"""

multiply = lambda a, b: a * b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Output :", multiply(a, b))