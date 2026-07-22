"""
    5: Design a Python application that creates two threads named Thread1 and Thread2.

    • Thread1 should display numbers from 1 to 50.
    • Thread2 should display numbers from 50 to 1 in reverse order.
    • Ensure that:
    ◦ Thread2 starts execution only after Thread1 has completed.
    • Use appropriate thread synchronizatio
"""

import threading

thread1_done = threading.Event()

def print_thread1():
    print("Thread1 started")
    for i in range(1, 51):
        print("Thread1:", i)
    print("Thread1 finished")
    thread1_done.set()   

def print_thread2():
    thread1_done.wait()  
    print("Thread2 started")
    for i in range(50, 0, -1):
        print("Thread2:", i)
    print("Thread2 finished")

thread1 = threading.Thread(target=print_thread1, name="Thread1")
thread2 = threading.Thread(target=print_thread2, name="Thread2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished execution.")