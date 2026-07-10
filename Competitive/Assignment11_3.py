# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

num = int(input("Enter a number: "))

# Convert to positive in case of negative input
num = abs(num)

digit_sum = 0
temp = num

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

print("Sum of digits:", digit_sum)