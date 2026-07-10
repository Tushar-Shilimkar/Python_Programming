"""Write a program which accept one number from user and return its factorial.

Input : 5           Output : 120  """

def factorial(no):
    result = 1
    for i in range(1, no + 1):
        result *= i
    return result

num = int(input("Input : "))
print("Output :", factorial(num))