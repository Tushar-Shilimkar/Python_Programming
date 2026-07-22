"""
    Write a program which contains filter(), map() and reduce() in it. Python application which
    contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which greater than or equal to 70 and less than or equal to
    90. Map function will increase each number by 10. Reduce will return product of all that numbers.

    Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter = [76, 89, 86, 90, 70]
    List after map = [86, 99, 96, 100, 80]
    Output of reduce = 6538752000
"""

from functools import reduce

num_list = list(map(int, input("Enter numbers separated by space: ").split()))
print("Input List =", num_list)

filtered_list = list(filter(lambda x: x >= 70 and x <= 90, num_list))
print("List after filter =", filtered_list)

mapped_list = list(map(lambda x: x + 10, filtered_list))
print("List after map =", mapped_list)

result = reduce(lambda x, y: x * y, mapped_list)
print("Output of reduce =", result)