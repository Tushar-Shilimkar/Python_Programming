"""
    Write a program which accept N numbers from user and store it into List. Accept one another
    number from user and return frequency of that number from List.

    Input : Number of elements : 11
    Input Elements : 13 5 45 7 4 56 5 34 2 5 65
    Element to search : 5
    Output : 3
"""
def main():
    n = int(input("Number of elements : "))
    elements = []
    
    print("Input Elements : ")
    for i in range(n):
        num = int(input())
        elements.append(num)
    
    target = int(input("Element to search : "))
    
    count = 0
    for num in elements:
        if num == target:
            count += 1
    
    print("Output :", count)

if __name__ == "__main__":
    main()