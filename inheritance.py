# inherritance in python
# it is one of the most importent feature of python which simulates the real world concept of inheritance. it specifies that the child object acquires all properties and behaviour of parent 
# by using inheritance we can create class which can use all the properties and behaviour of another class

class A:
    def __init__(self,name):
        self.name=name

class B(A):
    def __init__(self,roll):
        self.roll=roll

p=B(21)
print(p.roll)

r=A("praktik")
print(r.name)

q=A("narayan")
print(q.name)