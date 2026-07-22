"""
    3: Design a Python application that creates two threads named EvenList and OddList.

    • Both threads should accept a list of integers as input.
    • The EvenList thread should:
    • Extract all even elements from the list.
    • Calculate and display their sum.
    • The OddList thread should:
    • Extract all odd elements from the list.
    • Calculate and display their sum.
    • Threads should run concurrently.
"""
import threading

def even_list(numbers):
    print("EvenList Thread started")
    evens = [x for x in numbers if x % 2 == 0]
    even_sum = sum(evens)
    print("Even elements:", evens)
    print("Sum of even elements =", even_sum)
    print("EvenList Thread finished")

def odd_list(numbers):
    print("OddList Thread started")
    odds = [x for x in numbers if x % 2 != 0]
    odd_sum = sum(odds)
    print("Odd elements:", odds)
    print("Sum of odd elements =", odd_sum)
    print("OddList Thread finished")

num_list = list(map(int, input("Enter numbers separated by space: ").split()))
print("Input List =", num_list)

even_thread = threading.Thread(target=even_list, args=(num_list,), name="EvenList")
odd_thread = threading.Thread(target=odd_list, args=(num_list,), name="OddList")

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Both threads have finished execution.")