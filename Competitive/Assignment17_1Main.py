"""Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user. """

import Assignment17_1Arithmatic

def main():
    No1 = float(input("Enter the first number: "))
    No2 = float(input("Enter the second number: "))

    print("\n--- Results ---")
    print(f"Addition ({No1} + {No2})       = {Assignment17_1Arithmatic.Add(No1, No2)}")
    print(f"Subtraction ({No1} - {No2})    = {Assignment17_1Arithmatic.Sub(No1, No2)}")
    print(f"Multiplication ({No1} * {No2}) = {Assignment17_1Arithmatic.Mult(No1, No2)}")
    print(f"Division ({No1} / {No2})       = {Assignment17_1Arithmatic.Div(No1, No2)}")


if __name__ == "__main__":
    main()