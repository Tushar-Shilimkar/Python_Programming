"""Write a program which accept number from user and print that number of “*” on screen.

Input : 5           Output : * * * * *  """

No = int(input("Enter a number: "))

for i in range(No):
    print("*", end="    ")