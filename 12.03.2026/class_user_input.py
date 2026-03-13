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
        return self.calculate()/3
        
    def rank(self):
        if self.calavg()>=75:
            return "A"
        elif self.calavg()>=65:
            return "B"
        elif self.calavg()>=55:
            return "C"
        elif self.calavg()>=45:
            return "S"
        else :
            return "F"
        
    def display(self):    
        print("My id is"+str(self.id))
        print("My name is"+self.name)
        print("My total is"+str(self.calculate()))
        print("My avg is"+str(self.calavg()))
        print("My rank is"+self.rank())

sname=input("Enter your name:")
sid=int(input("Enter your id:"))
m1=int(input("Enter your mark1:"))
m2=int(input("Enter your mark2:"))
m3=int(input("Enter your mark3:"))

stu1=student(sid,sname)
stu1.marks(m1,m2,m3)
stu1.display()