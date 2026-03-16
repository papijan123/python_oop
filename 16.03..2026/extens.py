class A:
    def __init__(self):
        self.x=20
        self.z=50
    def getx(self):
        print("ax:"+str(self.x))
    def getz(self):
        print("zx:"+str(self.z))
        
        
class B(A):
    def __init__(self):
        super().__init__()
        self.y=30
    def gety(self):
        print("bx:"+str(self.y))
        
obj2=B()
obj2.getx()
obj2.gety()
obj2.getz()   
