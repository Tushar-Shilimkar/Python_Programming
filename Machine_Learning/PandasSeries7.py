import pandas as pd

def main():
    sobj = pd.Series([27000,32000], index = ["Amit","Sagar","Pooja"])

    print(sobj)

if __name__ == "__main__":
    main()