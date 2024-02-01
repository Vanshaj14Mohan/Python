#1: Grade students based on their marks:

marks = int(input("Enter student marks"))

if(marks >=90):
    grade = "A"
elif(marks >=80 and marks <90):
    grade = "B"
elif(marks >=70 and marks <80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student ->",grade)

#2: Program to check number entered by user is odd or even.

num = int(input("Enter a number"))

if(num%2 == 0):
    print("number is even")
else:
    print("number is odd")

print("--"*10)

#3: Program to find greatest of three numbers entered by the user.

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

if(num1 >= num2 and num1>= num3):
    print("First number is greatest")
elif(num2 >= num1 and num2 >= num3):
    print("Second number is greatest")
else:
    print("Third number is greatest")

print("--" *10)

#4:Program to find greatest of four numbers entered by the user.

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
num4 = int(input("Enter fourth number"))

if(num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("First number is greatest")
elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
    print("Second number is greatest")
elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
    print("Third number is greatest")
else:
    print("Fourth number is highest")

print("--" *10)

#5: Program to check whether a number is a multiple of 7 or not.

x = int(input("Enter a number"))

if(x%7 ==0):
    print("Number is multiple of 7")
else:
    print("Number is not a multiple of 7")

print("--" *10)