#Class and Instance Attributes

class Student:

    college_name = "ABC College"
    name = "anonymous" #class attribute
    
    #Parameterized constructor
    def __init__(self, name, marks):  #self parameter is a reference to current instance of the class, and is used to access variables that belongs to that class.
        self.name = name #obj attribute -> obj attribute > class attribute
        self.marks = marks
        print("New student added in database..")

#Creating object(instance)
s1 = Student("user", 92)
print(s1.name)#same as self-> ie self and this value refers to same location

#METHODS -> Methods are functions that belong to objects.

class Student:

    college_name = "XYZ College"

    def __init__(self, name, marks):  #self parameter is a reference to current instance of the class, and is used to access variables that belongs to that class.
        self.name = name #obj attribute -> obj attribute > class attribute
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("user", 92)
s1.welcome()
print(s1.get_marks())


