#del keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Alex")
print(s1.name) #shows the name

del s1
#print(s1.name) #now it will show error -> s1 not defined

#Private like attributes & methods
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # add __ before self. to make it private & we can't access it outside of the class

    def reset_pass(self):
        print(self.__acc_pass) #It will work coz it's inside the class

acc1 = Account("12345", "abcd")
#It will show us deatils of user account no & password
print(acc1.acc_no)
print(acc1.acc_pass)
#but if we want to hide it then
#print(acc1.__acc_pass) #Will show error coz we made it private 
#print(acc1.reset_pass()) #We can use it here

#We can make methods attributes & methods both private
#Private attributes & methods are meant to be used within the class and are not accessible from outside the class.
class Person: 
    __name="xyz" #attribute

    def __hello():
        print("Hello check") #methods

p1= Person()
print(p1.__name) #error coz of double underscore
print(p1.__hello()) #shows error of same reason



