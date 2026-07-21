"""
    Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

    Input : Number of elements : 6
    Input Elements : 13   5   45   7   4   56
    Output : 130
"""
def main():
    no = int(input("Number of elements : "))
    elements = []

    print("Input Elements : ")
    for i in range(no):
        num = int(input())
        elements.append(num)
    
    total = sum(elements)
    print("Output :", total)

if __name__ == "__main__":
    main()