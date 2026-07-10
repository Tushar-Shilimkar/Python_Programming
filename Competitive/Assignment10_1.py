#   Write a program which accepts one number and prints multiplication table of that number.

No = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{No} x {i} = {No * i}")