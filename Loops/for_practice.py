#1 -> Print elements of the following list using a loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
for el in list:
    print(el)
print("--"*10)

#2 -> Seacrch for a number x in this tuple using loop
tup = (10, 12, 15, 20, 25, 40, 50, 85, 90, 100)
idx = 0
x = 40
for el in tup:
    if (el == x):
        print("element found at idx", idx)
        break #in case if there were same numbers at different indexes.
    idx +=1

#3 ->Print sum of n natural numbers using for loop
n = 8
sum =0
for i in range(1, n+1):
    sum += i
print("total sum is", sum)
print("--"*10)

#4 -> Print factorial of first n numbers using for loop
n =7
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial =", fact)
