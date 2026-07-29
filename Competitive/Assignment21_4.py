"""
    Write a program that calculates 1^5+2^5+3^5+.....+N^5
    for multiple values of N simultaneously using Pool.

    Input
        [1000000,2000000,3000000,4000000]
    Measure total execution time.
"""
import time
from multiprocessing import Pool

def sum_of_fifth_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5
    return (n, total)

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    start_time = time.time()

    with Pool() as pool:
        results = pool.map(sum_of_fifth_powers, numbers)

    end_time = time.time()

    print(f"{'N':<12}{'Sum of 5th Powers'}")
    for n, total in results:
        print(f"{n:<12}{total}")

    print(f"\nTotal Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()