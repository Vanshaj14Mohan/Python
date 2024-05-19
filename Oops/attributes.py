#Class and Instance Attributes

class Student:
    
    #Parameterized constructor
    def __init__(self, fullname, marks):  #self parameter is a reference to current instance of the class, and is used to access variables that belongs to that class.
        self.name = fullname
        self.marks = marks
        print("New student added in database..")

#Creating object(instance)
s1 = Student("user", 92)
print(s1.name, s1.marks)#same as self-> ie self and this value refers to same location

s2 = Student("demo", 95)
print(s2.name, s2.marks)
