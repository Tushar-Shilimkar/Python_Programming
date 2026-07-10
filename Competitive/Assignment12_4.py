# Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


def main():
    num = int(input("Enter a number: "))
    print_numbers(num)


if __name__ == "__main__":
    main()