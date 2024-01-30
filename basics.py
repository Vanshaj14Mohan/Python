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
