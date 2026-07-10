# Write a program which contains one function ChkGreater() that accepts two numbers
# and prints the greater number.


def ChkGreater(a, b):
    if a > b:
        print(a, "is greater")
    elif b > a:
        print(b, "is greater")
    else:
        print("Both numbers are equal")

No1 = float(input("Enter first number: "))
No2 = float(input("Enter second number: "))
ChkGreater(No1, No2)