import os

def main():
    for folderName, SubFolder, FileName in os.walk("marvellous"):
        print("Folder Name : ",folderName)

        for subf in SubFolder:
            print("SubFolder Name : ",subf)

if __name__ == "__main__":
    main()