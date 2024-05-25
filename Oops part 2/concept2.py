#Inheritance -> When one class(child/derived) dervies the properties & methods of another class(Parent/base)
class Car:
    #2 methods-> start & stop
    color="black"
    @staticmethod
    def start():
        print("car started")

    def stop():
        print("car stopped")

class TataCar(Car): #using inheitance here
    def __init__(self,name):
        self.name = name

car1 = TataCar("Punch")
car2 = TataCar("Nexa")

print(car1.name)
print(car2.name)
print(car1.color)
#now
print(car2.start())#will show car started