"""Write a program which accept one number and display below pattern.

Input  : 5
Output : 1 2 3 4 5
         1 2 3 4 5
         1 2 3 4 5
         1 2 3 4 5
         1 2 3 4 5   """

no = int(input("Input : "))

for i in range(no):
    for j in range(1, no + 1):
        print(j, end="  ")
    print()