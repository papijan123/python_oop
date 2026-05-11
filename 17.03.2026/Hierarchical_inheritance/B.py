from A import A

class B(A):
    
    def __init__(self):
        super().__init__()
        self.y=30
    
    def gety(self):
        print("y:"+str(self.y))