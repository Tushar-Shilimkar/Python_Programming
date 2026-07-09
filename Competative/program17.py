# Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def get_factors(n):
    n = abs(n)
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors


def print_factors(n):
    factors = get_factors(n)
    print(f"Factors of {n}: {factors}")


def main():
    num = int(input("Enter a number: "))
    print_factors(num)


if __name__ == "__main__":
    main()