# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 
    return a / b


def print_results(a, b):
    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    print(f"Division: {a} / {b} = {divide(a, b)}")


def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print_results(num1, num2)


if __name__ == "__main__":
    main()