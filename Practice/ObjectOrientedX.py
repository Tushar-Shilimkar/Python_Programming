class Arithmatic:
    def Addition(self, No1, No2):
        Ans = No1 + No2
        return Ans
    
    # Ret = Addition(self, Value1, Value2)
    # Ret = Addition(Aobj, Value1, Value2)

    def Substraction(self, No1, No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmatic()

print("Enter First Number : ")
Value1 = int(input())

print("Enter Second Number : ")
Value2 = int(input())

Ret = Aobj.Addition(Value1, Value2)         
print("Addition is : ",Ret)

Ret = Aobj.Substraction(Value1, Value2)    
print("Substraction is : ",Ret)
