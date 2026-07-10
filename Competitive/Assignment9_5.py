#  Write a program which accepts one number and checks whether it is divisible by 3 and 5

def check_divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "is divisible by both 3 and 5")
    else:
        print(num, "is NOT divisible by both 3 and 5")

no = int(input("Enter a number: "))
check_divisible(no)