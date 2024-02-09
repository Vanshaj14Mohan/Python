#Introduction to while loop
#Print hello 5 times
count = 1 #here count -> iterator,
while count <=5:
    print("hello")
    count += 1
print(count) #6
 
#Print good 7 times 
i = 1 #i -> iterator here
while i <=7:
    print("good")
    i += 1
print(i)#8

#Print nice 5 times and it's value everytime
x = 1
while x<=5:
    print("nice", x) #nice 1.....nice 5
    x += 1
print(x)#6

#Print numbers from 1-10 using while loop
i = 1
while i<=10:
    print(i)
    i += 1

#Print numbers from 5-1 ie. reverse form
i = 5
while i>=1:
    print(i)
    i-=1
print("--"*10)

#using break statment
#print number from 1-5 but quit after reaching 3
i =1
while i<=5:
    print(i)
    if(i ==3):
        break
    i += 1
print("end of loop")

#Print 1-5 skip 3 number in that
i =0
while i<=5:
    if(i ==3):
        i += 1
        continue #skip, will skip three count 
    print(i)
    i += 1
print("end of loop")
