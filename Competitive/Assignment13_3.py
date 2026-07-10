# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def is_perfect_number(n):
    if n <= 0:
        return False
    divisor_sum = 0
    i = 1
    while i < n:
        if n % i == 0:
            divisor_sum += i
        i += 1
    return divisor_sum == n


def main():
    num = int(input("Enter a number: "))
    if is_perfect_number(num):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()