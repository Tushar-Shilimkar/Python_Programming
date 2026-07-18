import os

def main():
    for folderName, SubFolder, FileName in os.walk("marvellous"):
        for fname in FileName:
            print("FileName :",fname)

if __name__ == "__main__":
    main()