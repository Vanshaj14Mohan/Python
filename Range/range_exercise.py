#Print using for and range()
#1 -> Print numbers from 1 to 100
for i in range(1, 101):
    print(i)
print("--"*10)

#2 -> Print numbers from 100 to 1
for x in range(100, 0, -1): # -1 ie. decrease 1 value everytime, -> step size can be neagtive too.
    print(x)
print("--"*10)

#3 -> Print multiplication table of a number n
n = int(input("enter a number"))
for i in range(1,11):
    print(n * i)
print("--"*10)