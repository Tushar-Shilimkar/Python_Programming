def main():
    try:
        fobj = open("Demo.txt","r")    
        print("File gets opened")

        Data = fobj.read()      # read all data
        
        print(Data)

        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()