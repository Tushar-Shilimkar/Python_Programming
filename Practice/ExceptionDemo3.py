def main():
    Ans = 0

    try:
        print("Enter First number : ")
        No1 = int(input())

        print("Enter Second number : ")
        No2 = int(input())

        Ans = No1 / No2 

        print("Division is Succesful")

    except ZeroDivisionError as zobj:
        print("Exception Occured due to second operand is zero : ",zobj)

    except ValueError as vobj:
        print("Exception occured due to invalid datatype: ",vobj)

    print("Result is : ",Ans)

if __name__ == "__main__":
    main()