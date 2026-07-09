no = 11         # Global Variable

def Display():
    global no   # use global variable
    no = 21     # update Global Variable
    print("From Display :",no)  

print("Before : ",no)       
Display()
print("After : ",no)        
