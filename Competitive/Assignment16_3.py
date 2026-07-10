"""Write a program which contains one function named as Add() which accepts two numbers
   from user and return addition of that two numbers.
   
   Input : 11, 5         Output : 16 """

def Add(No1, No2):
    return No1 + No2


Ret1 = int(input("Enter first number: "))
Ret2 = int(input("Enter second number: "))

result = Add(Ret1, Ret2)
print("Output:", result)