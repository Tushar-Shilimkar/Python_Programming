"""
    5.Write a program which contains filter(), map() and reduce() in it. Python application which
    contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
    return Maximum number from that numbers. (You can also use normal functions instead of
    lambda functions).

    Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
    List after filter = [2, 11, 17, 23, 31]
    List after map = [4, 22, 34, 46, 62]
    Output of reduce = 62
"""

from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num_list = list(map(int, input("Enter numbers separated by space: ").split()))
print("Input List =", num_list)

filtered_list = list(filter(is_prime, num_list))
print("List after filter =", filtered_list)

mapped_list = list(map(lambda x: x * 2, filtered_list))
print("List after map =", mapped_list)

result = reduce(lambda x, y: x if x > y else y, mapped_list)
print("Output of reduce =", result)