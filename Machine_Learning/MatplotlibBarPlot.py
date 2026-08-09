import matplotlib.pyplot as plt

def main():
    language = ["C", "C++", "Java", "Python"]
    student = [30,40,35,55]

    plt.bar(
        language,                   # Value of X axis
        student,                    # Value of Y axis
        width=0.6,                  # Width of bar
        edgecolor = "black",        # border color of bars
        linewidth = 1,              # width of bar border
        alpha = 0.8,                # transperance 0.0 to 1.0
        label = "Students"          # legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Language")
    plt.ylabel("Number of Student")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main(),