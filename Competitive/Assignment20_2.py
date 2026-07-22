"""
    Design a Python application that creates two threads named EvenFactor and OddFactor.

    • Both threads should accept one integer number as a parameter.
    • The EvenFactor thread should:
    • Identify all even factors of the given number.
    • Calculate and display the sum of even factors.
    • The OddFactor thread should:
    • Identify all odd factors of the given number.
    • Calculate and display the sum of odd factors.
    • After both threads complete execution, the main thread should display the message:
      “Exit from main”
"""

import threading

def even_factor(n):
    even_factors = [i for i in range(1, n + 1) if n % i == 0 and i % 2 == 0]
    even_sum = sum(even_factors)
    print("EvenFactor Thread started")
    print("Even factors of", n, ":", even_factors)
    print("Sum of even factors =", even_sum)
    print("EvenFactor Thread finished")

def odd_factor(n):
    odd_factors = [i for i in range(1, n + 1) if n % i == 0 and i % 2 != 0]
    odd_sum = sum(odd_factors)
    print("OddFactor Thread started")
    print("Odd factors of", n, ":", odd_factors)
    print("Sum of odd factors =", odd_sum)
    print("OddFactor Thread finished")

num = int(input("Enter a number: "))

even_thread = threading.Thread(target=even_factor, args=(num,), name="EvenFactor")
odd_thread = threading.Thread(target=odd_factor, args=(num,), name="OddFactor")

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Exit from main")