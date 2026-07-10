"""Write a program which accepts marks and displays grade.
Condition Example:
• ≥ 75 → Distinction
• ≥ 60 → First Class
• ≥ 50 → Second Class
• < 50 → Fail"""

def get_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    marks = float(input("Enter marks: "))
    grade = get_grade(marks)
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()