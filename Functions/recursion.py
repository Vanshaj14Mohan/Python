#Recursion 
#When a person calls itself repeatedly.

#1. Print number from n to 1 backwards using recurion.

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(6) 