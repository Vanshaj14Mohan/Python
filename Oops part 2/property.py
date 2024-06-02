#using property decorator
print("property decorator")
class Student:
    def __init__(self,maths,cs,stats):
        self.maths = maths
        self.cs = cs
        self.stats = stats
        self.percentage = str((self.maths + self.cs + self.stats)/3) + "%"

stu1 = Student(98,95,95)
print(stu1.percentage)