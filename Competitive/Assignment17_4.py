"""Write a program which accept one number form user and return addition of its factors.

Input : 12          Output : 16 (1+2+3+4+6)  """

no = int(input("Input : "))

total = 0
for i in range(1, no):
    if no % i == 0:
        total += i

print("Output :", total)