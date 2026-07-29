"""
    Write a program that calculates factorials of multiple numbers
    simultaneously using Pool.map().
    
    Input
        [10,15,20,25]
    Display
        • Process ID
        • Input Number
        • Factorial
"""
import os
import math
from multiprocessing import Pool

def factorial_worker(n):
    pid = os.getpid()
    result = math.factorial(n)
    return (pid, n, result)

def main():
    numbers = [10, 15, 20, 25]

    with Pool() as pool:
        results = pool.map(factorial_worker, numbers)

    print(f"{'Process ID':<12}{'Input Number':<15}{'Factorial'}")
    for pid, n, fact in results:
        print(f"{pid:<12}{n:<15}{fact}")

if __name__ == "__main__":
    main()