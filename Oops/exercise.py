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

#Create account class with 2 attributes - balance & account no .
#Create methods for debit, credit & printing the values
class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    #Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited" )
        print("total balance =", self.get_balance())

    #Credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited" )
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 1457)
# print("Account balance" , acc1.balance)
# print("Account number" , acc1.account_no)       
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)
acc1.debit(5000)
