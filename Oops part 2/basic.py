#del keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Alex")
print(s1.name) #shows the name

del s1
#print(s1.name) #now it will show error -> s1 not defined