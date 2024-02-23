#Functions are block of statements that perform a specfic task.
#Making function for adding two numbers.

def cal_sum (a, b):
    sum = a+b
    print(sum)
    return sum

print("For addition")
cal_sum(2, 5)
print("--"*5)

#For Multiplication
def mul_fun (a, b):
    mul = (a * b)
    print(mul)
    return mul

print("for multiplication")
mul_fun(2, 8)
print("--"*5)

#For substraction
def sub_fun (a, b):
    subs = (a - b)
    print(subs)
    return subs

print("For substraction")
sub_fun(40, 32)
print("--"*5)


#Another way to implement this, 
# For divison
print("For divison")
def div_find(a,b):
    return a % b 
div = div_find(98, 12)
print(div) #returns remainder
print("--"*5)