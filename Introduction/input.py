#Now to see how input statement works
name = input("Enter your name:")
print("Welcome", name)
age = input("Enter your age:")
print("Your age is", age)

#Note: input() => result for input statement is always a string
price = input("Enter price:")
print(type(price), price) #Type=> str, same goes for integer and float values.
value = int(input("Enter a random value"))
print(type(value), value) #Now it will show type as integer

value2 = float(input("Enter a value:"))
print(type(value2), value2) #Type=> Float

