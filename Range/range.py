# range()
#Range functions returns a sequence of numbers, starting from 0 by default, and increases by 1(by default), and stops before a specified number
#range(start?, stop, step?) ?->optional not necessary/
for i in range(10): #will print values from 0-9, excluding 10, range(stop)
    print(i)
print("--"*10)

for i in range(0, 8): #range(start, stop)
    print(i) #0-7
print("--"*10)

for i in range (0, 10, 2): #range(start, stop, step-size)
    print(i) #0,2,4,6,8 -> increase two after every starting value.
print("--"*10)

#small task, print even numbers from 2-20 using range
for i in range(2, 21, 2):
    print(i)
print("--"*10)

#print odd numbers from 1-20 using range
for i in range(1, 20, 2):
    print(i)
print("--"*10)