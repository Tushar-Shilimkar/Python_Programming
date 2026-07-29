"""
    For every number in the given list, count how many prime numbers
    exist between 1 and N using multiprocessing Pool.

    Example
        10000
        20000
        30000
        40000
    Display total prime count for each number.
"""
from multiprocessing import Pool

def count_primes(n):
    if n < 2:
        return (n, 0)

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return (n, sum(sieve))

def main():
    numbers = [10000, 20000, 30000, 40000]

    with Pool() as pool:
        results = pool.map(count_primes, numbers)

    print(f"{'N':<10}{'Prime Count'}")
    for n, count in results:
        print(f"{n:<10}{count}")

if __name__ == "__main__":
    main()