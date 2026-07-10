# Write a program which accepts one number and prints binary equivalent.

def to_binary(n):
    binary_digits = ""
    while n > 0:
        binary_digits = str(n % 2) + binary_digits
        n = n // 2
    return binary_digits


def main():
    num = int(input("Enter a number: "))
    print(f"Binary equivalent: {to_binary(num)}")


if __name__ == "__main__":
    main()