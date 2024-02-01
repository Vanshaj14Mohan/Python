#if-elif-else(SYNTAX)

light ="green" #It will print go now;

if(light == "red"):
    print("Stop, don't go ahead")
elif(light == "yellow"):
    print("Wait, look around")
elif(light == "green"):
    print("Go now")

print("--"*10)

age =22

if(age >=18):
    print("can apply for license")
else:
    print("cannot apply for license")

print("--"*10)

#Nesting in conditional statements

age = 95
if(age >=18):
    if(age >=85):
       print("cannot apply for test at this age ")
    else:
      print("Can apply for test")
else:
 print("Cannot apply for test")


