#Operator overloading
# eg-> + operators works differentely with different datatypes
print(1+2)#3
print(type(1))# shows class int

print("good" + "day")#concatenate
print(type("good"))# shows class string

print([1,2,3] + [4,5,6])#merge
print(type([1,2,3])) #shows class list
#So basically same operator is allowed to have different meaning acc to context.. 

#Creating a complex class
print("Complex class")
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

#creating a complex number
num1 = Complex(2,5)
num1.showNumber()

num2 = Complex(5,7)
num2.showNumber()

#Now creating a function to add complex numbers using polymorphism