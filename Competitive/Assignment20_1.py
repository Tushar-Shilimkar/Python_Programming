"""
    1: Design a Python application that creates two separate threads named Even and Odd.

    • The Even thread should display the first 10 even numbers.
    • The Odd thread should display the first 10 odd numbers.
    • Both threads should execute independently using the threading module.
    • Ensure proper thread creation and execution.
"""

import threading

import threading

even_done = threading.Event()

def print_even():
    print("Even Thread started")
    for i in range(1, 11):
        print("Even:", i * 2)
    print("Even Thread finished")
    even_done.set()  

def print_odd():
    even_done.wait()   
    print("Odd Thread started")
    for i in range(1, 11):
        print("Odd:", (i * 2) - 1)
    print("Odd Thread finished")

even_thread = threading.Thread(target=print_even, name="Even")
odd_thread = threading.Thread(target=print_odd, name="Odd")

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Both threads have finished execution.")