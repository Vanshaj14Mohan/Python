#1 Abstraction -> Hiding the implementation details of a class and only showing the essential features to the user.
#Example:
class Car:
    def __int(self):
        self.acc= False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc= True
        self.clutch= True
        print("car started now")

car1= Car()
car1.start()

#2 Encapsulation -> Wrapping up of data and functions into a single unit(object). 
