#using property decorator
print("property decorator")
class Student:
    def __init__(self,maths,cs,stats):
        self.maths = maths
        self.cs = cs
        self.stats = stats
        self.percentage = str((self.maths + self.cs + self.stats)/3) + "%"

    def calPercentage(self):
        self.percentage = str((self.maths + self.cs + self.stats)/3) + "%"

stu1 = Student(98,95,95)
print(stu1.percentage) #will print the average

stu1.maths = 92
print(stu1.maths)
stu1.calPercentage()
print(stu1.percentage)