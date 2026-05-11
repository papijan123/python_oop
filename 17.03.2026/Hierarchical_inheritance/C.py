from A import A

class C(A):
    
    def __init__(self):
        super().__init__()
        self.z=60
    def getz(self):
        print("z:"+str(self.z))