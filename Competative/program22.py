# Write a program which accepts radius of circle and prints area of circle.

import math


def calculate_area(radius):
    return math.pi * radius ** 2


def main():
    radius = float(input("Enter radius: "))
    area = calculate_area(radius)
    print(f"Area of circle: {area:.2f}")


if __name__ == "__main__":
    main()