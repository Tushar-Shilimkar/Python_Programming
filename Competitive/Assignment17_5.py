"""Write a program which accept one number for user and check whether number is prime or not.

Input : 5 Output : It is Prime Number  """

no = int(input("Input : "))

is_prime = True
if no < 2:
    is_prime = False
else:
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            is_prime = False
            break

if is_prime:
    print("Output : It is Prime Number")
else:
    print("Output : It is not a Prime Number")