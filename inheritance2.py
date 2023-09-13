class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print(self.name,self.age)

# child class

class student(person):
    def __init__(self, name, age):
        self.sname=name
        self.sage=age

    # inheritance the properties of parent class
        super().__init__("prak",16)

    def displayInfo(self):
        print(self.sname,self.sage)

n=student("narayan",20)
n.display()
n.displayInfo()