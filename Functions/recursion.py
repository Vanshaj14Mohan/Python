#Recursion 
#When a person calls itself repeatedly.

#1. Print number from n to 1 backwards using recurion.
def num(n):
    if(n == 0): #base case
        return
    print(n)
    num(n-1)
num(6) 

#2. Print n factorial of a number
def fac(n):
    if(n == 0 or n ==1):
        return 1
    else:
        return n * fac(n-1)

print(fac(7))
print("--"*10)

#3. Write a recursive function to calculate the sum of first n natural numbers.
def natural_no(n):
    if(n == 0):
        return 0
    return natural_no(n-1) + n
sum =natural_no(7)
print(sum)

#4. Write a recursive function to print all elements in a list. hint use list & index as paramter
def list_no(list, idx =0):
    if(idx ==len(list)):
        return 
    print(list[idx])
    list_no(list, idx+1)

languages =["Javascript", "C++", "Python", "C", "Java"]
list_no(languages)