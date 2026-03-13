class student:

    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    def marks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def calculate(self):
        return self.m1+self.m2+self.m3
    
    def calavg(self):
        return self.calculate()//3
        
    def rank(self):
        avg=self.calavg()
        if avg>=75:
            return "A"
        elif avg>=65:
            return "B"
        elif avg>=55:
            return "C"
        elif avg>=45:
            return "S"
        else :
            return "F"
        
    def display(self):
    
        print("my id is"+str(self.id))
        print("my name is"+self.name)
        print("my total is"+str(self.calculate()))
        print("my avg is"+str(self.calavg()))
         print("my rank is"+self.rank())

stu1=student(1000,"papijan") 
stu1.marks(72,75,78)
stu1.display()