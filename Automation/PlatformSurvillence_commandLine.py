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

def main():
    Border = "*"*60
    print(Border)
    print("----- Marvellous Platform Survillence System-----")
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
        pass

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as argument are not watching.")
        print("Please use --h or --u flag for getting more datails.")

    print(Border)
    print("-----Thank you for using our Automation System-----")
    print(Border)

if __name__ == "__main__":
    main()