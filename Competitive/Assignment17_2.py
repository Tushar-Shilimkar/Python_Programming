"""Write a program which accept one number and display below pattern.

Input  : 5
Output : * * * * *
         * * * * *
         * * * * *
         * * * * *
         * * * * *  """

no = int(input("Input : "))

for i in range(no):
    print("*    " * no)