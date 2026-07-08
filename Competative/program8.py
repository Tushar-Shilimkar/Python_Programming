#  Write a program which accepts one number and prints factorial of that number.

no = int(input("Enter a number: "))

factorial = 1
for i in range(1, no + 1):
    factorial *= i

print(f"Factorial of {no} = {factorial}")