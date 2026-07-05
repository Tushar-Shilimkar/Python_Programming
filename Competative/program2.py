def ChkGreater(a, b):
    if a > b:
        print(a, "is greater")
    elif b > a:
        print(b, "is greater")
    else:
        print("Both numbers are equal")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
ChkGreater(num1, num2)