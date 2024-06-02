#Inheritance -> When one class(child/derived) dervies the properties & methods of another class(Parent/base)
#Single Inheritance example:
print("Single Inheritance:")
class Car: #Parent class
    #2 methods-> start & stop
    color="black"
    @staticmethod
    def start():
        print("car started")

    def stop():
        print("car stopped")

#Child class
class TataCar(Car): #using inheitance here
    def __init__(self,name):
        self.name = name

car1 = TataCar("Punch")
car2 = TataCar("Nexa")

print(car1.name)
print(car2.name)
print(car1.color)
#now
print(car2.start())#will show car started

print("--"*20)

#Multilevel Inheritance
print("Multilevel Inheritance:")
class Car: #Parent class
    color="black"
    @staticmethod
    def start():
        print("car started")

    def stop():
        print("car stopped")

#Child class
class TataCar(Car): #using inheitance here
    def __init__(self,brand):
        self.brand = brand

class Nexa(TataCar):
    def __init__(self,type):
        self.type= type

car1 = Nexa("diesel")
car1.start()
print("--"*20)


#Multiple Inheritance
print("Multiple Inheritance:")
class A:
    varA = "Class A"

class B:
    varB = "Class B"

class C(A,B): #Class C inheriting propreties of class A and B
    varC = "Class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

print("--"*20)

#Super method
#super() method is used to access methods of the parent class
print("Super method..")
class Car: 
    def __init__(self,type): #Extra constructor
        self.type = type

    @staticmethod
    def start():
        print("car started")

    def stop():
        print("car stopped")

class ToyotaCar(Car): 
    def __init__(self,name,type):
        super().__init__(type) #using super method
        self.name = name
        super().start()

car1 = ToyotaCar("Demo", "electric")
print(car1.type)
print("--"*20)

#Class method
#A class method is bound to the class & receives the class as an implicit first argument.
#Note-> A static method can't access or modify class state & generally for utility.
print("Class method")
class Person:
    name ="random"

    # def changeName(self,name):
    #      self.name = name
    #     Person.name = name
    #      or this ->self.__class__.name = "david" will give same result

    @classmethod #using class methods
    def changeName(cls,name):
        cls.name = name 

p1 = Person()
p1.changeName("david")
print(p1.name)
#print(Person.name) #Will give the old value of 
print(Person.name) #now it will show the name that we gave 


