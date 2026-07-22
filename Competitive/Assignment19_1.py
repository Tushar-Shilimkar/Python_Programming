"""
    Write a program which contains one lambda function which accepts one parameter and return power of two.

    Input : 4 Output : 16
    Input : 6 Output : 64
"""

power_of_two = lambda x: 2 ** x


n = int(input("Enter a number: "))
print("Output :", power_of_two(n))