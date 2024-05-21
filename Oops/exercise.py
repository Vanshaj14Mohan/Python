#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.
#Showing non static method-> that uses self parameter
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("Matthew Parker", [99, 95, 97])
s1.get_avg()

#We can also change the value of student if we want 
s1 = Student("Tom Hardy",[96, 95, 90])
s1.get_avg()

#Static methods -> Methods that don't use the self parameter(work at class level)
@staticmethod #decorator (@staticmethod -> converts a function into a static method) 
def hello():
    print("Hello")

hello()
