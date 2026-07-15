class Base:
    def __init__(self):
        print("Inside Base Constructor")

class Derived(Base):       
    def sun(self):
        print("Inside Derived sun")

dobj = Derived()

dobj.sun()