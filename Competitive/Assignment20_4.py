"""
    4: Design a Python application that creates three threads named Small, Capital, and Digits.

    • All threads should accept a string as input.
    • The Small thread should count and display the number of lowercase characters.
    • The Capital thread should count and display the number of uppercase characters.
    • The Digits thread should count and display the number of numeric digits.
    • Each thread must also display:
    • Thread ID
    • Thread Name
"""

import threading

def count_small(text):
    current_thread = threading.current_thread()
    count = sum(1 for ch in text if ch.islower())
    print("Thread ID:", current_thread.ident, "| Thread Name:", current_thread.name)
    print("Number of lowercase characters =", count)

def count_capital(text):
    current_thread = threading.current_thread()
    count = sum(1 for ch in text if ch.isupper())
    print("Thread ID:", current_thread.ident, "| Thread Name:", current_thread.name)
    print("Number of uppercase characters =", count)

def count_digits(text):
    current_thread = threading.current_thread()
    count = sum(1 for ch in text if ch.isdigit())
    print("Thread ID:", current_thread.ident, "| Thread Name:", current_thread.name)
    print("Number of numeric digits =", count)

input_string = input("Enter a string: ")
print("Input String =", input_string)

small_thread = threading.Thread(target=count_small, args=(input_string,), name="Small")
capital_thread = threading.Thread(target=count_capital, args=(input_string,), name="Capital")
digits_thread = threading.Thread(target=count_digits, args=(input_string,), name="Digits")

small_thread.start()
capital_thread.start()
digits_thread.start()

small_thread.join()
capital_thread.join()
digits_thread.join()

print("All threads have finished execution.")