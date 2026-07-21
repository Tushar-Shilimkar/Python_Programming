"""
    Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

    Input : Number of elements : 7
    Input Elements : 13   5   45   7   4    56  34
    Output : 56
"""
def main():
    no = int(input("Number of elements : "))
    elements = []
    
    print("Input Elements : ")
    for i in range(no):
        num = int(input())
        elements.append(num)
    
    max = elements[0]
    for num in elements:
        if num > max:
            max = num
    
    print("Output :", max)

if __name__ == "__main__":
    main()