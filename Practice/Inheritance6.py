class Base1:
    def fun(self):
        print("Inside Base1 Constructor")

class Base2:
    def gun(self):
        print("Inside Base2 Constructor")

class Derived(Base1, Base2):       
    def sun(self):
        print("Inside Derived sun")

dobj = Derived()
dobj.sun()
dobj.gun()
dobj.fun()