import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous"):
    Border = "*"*60
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    print("Log File gets created with name :",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("--------------- Marvellous Automation Script ------------------\n")
    fobj.write(Border+"\n\n")

    fobj.write("Files from the Directory are : \n\n")
    fobj.write(Border+"\n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at :"+timestamp)
    fobj.write("\n"+Border+"\n")

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
            schedule.every(1).minute.do(DirectoryScanner, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more Information")

    print (Border)
    print("------ Thank you for using  Marvellous Automation Script ------")
    print (Border)

if __name__ == "__main__":
    main()