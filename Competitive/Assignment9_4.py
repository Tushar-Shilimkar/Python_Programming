#  Write a program which accepts one number and prints cube of that number.

def cube(num):
    return num * num * num

no = int(input("Enter a number: "))
result = cube(no)
print(f"Cube of {no} is {result}")