# Write a program which accepts length and width of rectangle and prints area.

def calculate_area(length, width):
    return length * width


def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = calculate_area(length, width)
    print(f"Area of rectangle: {area}")


if __name__ == "__main__":
    main()