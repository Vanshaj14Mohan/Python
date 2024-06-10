#Q 1-> Define a circle class with radius r using the constructor. Define an Area() method of the class 
# which calculates the area of the circle. Define a Perimeter() method of the class which allows you to 
# calculate the perimeter of the circle.
print("Question 1")
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return (22/7) * 3.14 *self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
print("--"*20)

#Q 2-> Define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
#Create an Enginner class that inherits properties from Employee & has additional attributes: name & age.
print("Question 2")
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        super().__init__("Engineer", "IT", "80,000")

eng1 = Engineer("David", 30)
eng1.showDetails()
# e1 = Employee("manager", "management", "20,000")
# e1.showDetails()
print("--"*20)

#Q 3-> Create a class Order which stores item & it's price.
# Use Dunder function __gt__() to convey that:
#order1 > order2 if price of order1 > price of order2