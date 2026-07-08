#  Write a program which accepts one number and prints all even numbers till that number.

no = int(input("Enter a number: "))

for i in range(2, no + 1, 2):
    print(i)