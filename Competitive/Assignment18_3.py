"""
    Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

    Input : Number of elements : 4
    Input Elements : 13   5  45   7
    Output : 5
"""
def main():
    no = int(input("Number of elements : "))
    elements = []
    
    print("Input Elements : ")
    for i in range(no):
        num = int(input())
        elements.append(num)
    
    min = elements[0]
    for num in elements:
        if num < min:
            min = num
    
    print("Output :", min)

if __name__ == "__main__":
    main()