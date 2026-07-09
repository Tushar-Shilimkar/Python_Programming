# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

ch = input("Enter a character: ")

# Convert to lowercase for easy checking
ch = ch.lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")