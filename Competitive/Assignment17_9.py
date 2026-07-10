"""Write a program which accept number from user and return number of digits in that number.

Input : 5187934         Output : 7  """

no = int(input("Input : "))

count = 0
temp = abs(no)

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10
        count += 1

print("Output :", count)