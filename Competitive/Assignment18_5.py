"""
    Write a program which accept N numbers from user and store it into List. Return addition of all
    prime numbers from that List. Main python file accepts N numbers from user and pass each
    number to ChkPrime() function which is part of our user defined module named as
    MarvellousNum. Name of the function from main python file should be ListPrime().

    Input : Number of elements : 11
    Input Elements : 13 5 45 7 4 56 10 34 2 5 8
    Output : 54 (13 + 5 + 7 +2 + 5)
"""
import MarvellousNum

def ListPrime(elements):
    total = 0
    for num in elements:
        if MarvellousNum.ChkPrime(num):
            total += num
    return total

def main():
    n = int(input("Number of elements : "))
    elements = []
    
    print("Input Elements : ")
    for i in range(n):
        num = int(input())
        elements.append(num)
    
    result = ListPrime(elements)
    print("Output :", result)

if __name__ == "__main__":
    main()