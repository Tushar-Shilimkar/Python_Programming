#  Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

no = int(input("Enter a number: "))

is_prime = True

if no < 2:
    is_prime = False
else:
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{no} is a prime number")
else:
    print(f"{no} is not a prime number")