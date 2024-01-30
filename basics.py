#Normal print condition in python.
print("hello world!")
print(20+30)
print(50-20)
print(20*20)
print(10/5)
print(25%5)
print(2**9)

#Now how to use variables
name = "Vanshaj P Mohan"
age = 22
email = "Vanshajkumar145@gmail.com"
price = 25.90
print(name, age, email, price)

#To see the type of variables:
print(type(name))
print(type(age))
print(type(email))
print(type(price))

#To see datatypes
age = 22 #Integer datatype
amount = 88.25 #Float datatype 
order = True #Boolean datatype
new = None #None datatype

print((type(age)), (type(amount)), (type(order)), (type(new)))

#Now a small question, add two numbers
a = 10
b = 20
sum = a+b
print(sum)

#same for difference
a = 15
b = 10
diff = a-b
print(diff)

#Now types of operators in python
#Arithmetic operators
a = 7
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #gives remainder
print(a**b) #a^b

#Relational operators, gives true or false in output
a = 30
b = 20
print(a == b) #False
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print( b > a) #False
print(b != a) #True
print(a != b) #True

#Assignment operators
num = 10
#num = num + 10
num += 10 #short way to write above code
print("num :", num) #10+10 =>20
num2 = 20
num2 -=5
print("num2:", num2)#15
num3 = 20
num3 *=5
print("num3:", num3)#100
num4 = 35
num4 /=5
print("num4:", num4)#7.0
num5 = 45
num5 %= 10
print("num5:", num5)#5
num6 = 8
num6 **=4
print("num6:", num6)#4096

#Logical operators
#not operator => Gives the reverse answer, just the opposite
print(not False)
print(not True)
a = 25
b = 15
print(not (a>b)) #False
print(not (a<b)) #True

#and operator, gives true values when both operands have true values
val1 = True
val2 = True
print("And case test:", val1 and val2) #True
val3 = True
val4 = False
print("And case test:", val3 and val4) #False
 
#or operator, gives true value if any operand has true value
value1 = True
value2 = False
print("Or case test:", value1 or value2) #True
value3 = False
value4 = False
print("Or case test:", value3 or value4)# False
#we can apply this on values too
print("Or test case:", (a ==b) or (a>b))#True
