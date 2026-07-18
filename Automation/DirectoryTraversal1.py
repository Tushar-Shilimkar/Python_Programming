import os

def main():
    for folderName, SubFolder, FileName in os.walk("marvellous"):
        print(folderName)

if __name__ == "__main__":
    main()