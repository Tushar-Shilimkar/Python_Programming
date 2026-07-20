# python Automation.py --h
# python Automation.py --u
# python Automation.py Marvellous
# python Automation.py --d
# python Automation.py Marvellous Demo

import sys
import os

def DirectoryScanner(DirectoryPath):

    print("Files from the direcctory are :")

    fobj = open("MarvellousLog.txt","w")

    fobj.write("--------------- Marvellous Automation Script ------------------\n")

    fobj.write("Files from the Directory are : \n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")

    fobj.close()

def main():
    Border = "*"*63
    print(Border)
    print("--------------- Marvellous Automation Script ------------------")
    print (Border)
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation is used to travel the Directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the Script as")
            print("Python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            DirectoryScanner(sys.argv[1])
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more Information")

    print (Border)
    print("------ Thank you for using  Marvellous Automation Script ------")
    print (Border)

if __name__ == "__main__":
    main()