#  Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

no = int(input("Enter a number: "))

no = abs(no)  # handle negative numbers
count = 0

if no == 0:
    count = 1
else:
    while no > 0:
        no = no // 10
        count += 1

print(f"Count of digits = {count}")