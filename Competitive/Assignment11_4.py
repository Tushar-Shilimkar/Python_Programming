# Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

num = int(input("Enter a number: "))

# Handle negative numbers
negative = num < 0
num = abs(num)

reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if negative:
    reverse = -reverse

print("Reverse of the number:", reverse)