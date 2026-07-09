# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def print_numbers_reverse(n):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print()


def main():
    num = int(input("Enter a number: "))
    print_numbers_reverse(num)


if __name__ == "__main__":
    main()