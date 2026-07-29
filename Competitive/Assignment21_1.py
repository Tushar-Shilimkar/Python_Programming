"""
    Write a program that accepts a list of integers and uses Pool.map()
    to calculate the sum of squares from 1 to N for every element in the list.
    
    Example Input
        [1000000,2000000,3000000,4000000]
    Expected Output
        [333333833333500000,
        2666668666667000000,
        ...
        ]
"""
from multiprocessing import Pool

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def main(numbers):
    with Pool() as pool:
        results = pool.map(sum_of_squares, numbers)
    return results

if __name__ == "__main__":
    input_list = [1000000, 2000000, 3000000, 4000000]
    output = main(input_list)
    print(output)