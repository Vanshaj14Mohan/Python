#Q 1-> Define a circle class with radius r using the constructor. Define an Area() method of the class 
# which calculates the area of the circle. Define a Perimeter() method of the class which allows you to 
# calculate the perimeter of the circle.
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

#Q 2-> Define a Employee class with attributes role, department & salary. This class also has a showDetails() method.
#Create an Enginner class that inherits properties from Employee & has additional attributes: name & age.