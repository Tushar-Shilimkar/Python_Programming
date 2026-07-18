import schedule
import time
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script started")

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()          # run kahi pending asel tr
        time.sleep(1)                   # sleep 

    print("End of Automation script")

if __name__ == "__main__":
    main()