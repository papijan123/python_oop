from A import A
class B(A):
    def __init__(self):
        self.y=20
        super().__init__()
        
    def gety(self):
        print(self.y)
        
        
    