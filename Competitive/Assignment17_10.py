"""Write a program which accept number from user and return addition of digits in that number.

Input : 5187934         Output : 37     """

no = int(input("Input : "))

total = 0
temp = abs(no)

while temp > 0:
    digit = temp % 10
    total += digit
    temp = temp // 10

print("Output :", total)