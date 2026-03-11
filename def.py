class student:
	
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
        
    def display(self):
        print("my name is"+self.name)
        print("my id is"+str(self.id))
        


stu1=student("selvan",1234)
stu1.display()

stu2=student("papijan",1000)
stu2.display()