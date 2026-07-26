# python ProcessSurvillence.py 2 MarvellousLog
# python ProcessSurvillence.py time_intervel Folder_Name
#                   0               1              2
#len(sys.argv) -> 3

# ProcessSurvillence.py --h
# ProcessSurvillence.py --u
#           0            1
#len(sys.argv) -> 2

import psutil
import sys
import os
import time
import schedule

def PlatformSurvillence(FolderName):
    Border = "*"*60

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created Succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Platform Survillence System-----\n")
    fobj.write("Log File gets created at :"+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------- System Report -------------------\n")

    fobj.write("Number of active CPU cores : %s \n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("------------------ End of Log File ------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "*"*60
    print(Border)
    print("----- Marvellous Platform Survillence System-----\n")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation Script is used to perform")
            print("1 : It fetch the information of running processes")
            print("2 : It fetch the information about the primary storage as RAM")
            print("3 : It fetch the information about the secondary storage as HHD")
            print("4 : It fetch the information about the microprocessor")
            print("5 : It gets auto schedule periodically")
            print("6 : It maintains all records into log file")
            print("7 : It send the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to proceed as argument are not watching.")
            print("Please use --h or --u flag for getting more datails.")

    # Actual project code
    elif (len(sys.argv) == 3):
        # print("CPU Usage : ",psutil.cpu_percent())
        print("Schedular started Succesfully")
        print("Press Ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as argument are not watching.")
        print("Please use --h or --u flag for getting more datails.")

    print(Border)
    print("-----Thank you for using our Automation System-----")
    print(Border)

if __name__ == "__main__":
    main()