import os

def main():
    for folderName, SubFolder, FileName in os.walk("marvellous"):
        print("Folder Name : ",folderName)

        for subf in SubFolder:
            print("SubFolder Name : ",subf)

        for fname in FileName:
            print("FileName :",fname)

if __name__ == "__main__":
    main()