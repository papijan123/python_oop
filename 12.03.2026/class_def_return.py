class student:

    def __init__(self,fname,lname,id):
        self.fname=fname
        self.lname=lname
        self.id=id
    def getfullname(self):
        return self.fname+self.lname
        
    def display(self):
        print("my full name is"+self.getfullname())
        print("my name is"+self.lname)
        print("my id is"+str(self.id))
        
        
    
        
stu1=student("karunarasan","papijan",11000)
stu1.display()