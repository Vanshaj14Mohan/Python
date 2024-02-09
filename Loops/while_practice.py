#1 -> Print numbers from 1 to 100
i = 1
while i<=100:
    print(i)
    i +=1
print("--"*10)

#2 -> Print numbers from 100 to 1
i = 100
while i>=1:
    print(i)
    i -=1
print("--"*10)

#3 -> Print the multiplication table of number n
#Let's take n as 4
n = int(input("enter a number"))
x = 1
while x<=10:
    print(n*x)# n*x
    x +=1

#4 -> Print elements of the given list using loops
#[1,4,9,25,36,49,64,81,100]
nums =[1, 4, 9, 25, 36, 49, 64, 81, 100]
idx =0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1]...
    idx += 1

#5 -> Search for a number x in this tuple using loop:
#(1,4,9,25,36,49,64,81,100)
random = (1, 4, 9, 25, 36, 49, 64, 81, 100)
x= 36
i =0
while i < len(random):
    if(random[i] == x):
        print("Number found at idx:", i)
        break
    else:
        print("Not found")
    i +=1
print("end of loop")

#6 -> Print  1-10 numbers using while loop excluding even numbers in it.
i = 1
while i<10:
    if(i%2 == 0):
        i +=1
        continue
    print(i)
    i +=1
print("end of loop")

#7 -> Print  1-10 numbers using while loop excluding odd numbers in it.
i = 1
while i<=10:
    if(i%2 != 0):
        i +=1
        continue
    print(i)
    i +=1
print("end of loop")