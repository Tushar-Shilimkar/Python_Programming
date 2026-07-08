#  Write a program which accepts one number and prints sum of first N natural numbers.

no = int(input("Enter a number: "))

total = 0
for i in range(1, no + 1):
    total += i

print(f"Sum of first {no} natural numbers = {total}")