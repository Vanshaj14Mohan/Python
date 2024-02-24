#1. Function to count average of 3 numbers
def find_avg (a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return(avg)
find_avg(10, 20, 30)
print("--"*5)

#2. Program to print the length of a list.(list is the parameter).
print("length of list")
list = ["India", "Japan", "USA", "Russia", "France", "Canada", "UK"]
cities = ["Lucknow", "Tokyo", "Shibuya", "Paris", "New York", "London", "Amsterdam"]
def print_len (countries):
    print(len(countries))

print_len(list)#7
print_len(cities) #7

#3. Program to print elements of a list in a single line.(list is the parameter)
sub = ["Computer", "Maths", "English", "Science"]

def single_line(sub):
    for subjects in sub:
        print(subjects, end=" ")

# single_line(sub)
#4. Program to find the factorial of n.(n is parameter)

print("--"*10)
def fac_no (n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
fac_no(6)


#5. Program to convert USD into INR.
#1usd=83rupess
def convert(usd_value):
    inr_value = usd_value * 83
    print(usd_value, "USD=", inr_value, "INR")
convert(90)
print("--"*5)

#6. Program to check if number is even or odd using functions.
def numbers(n):
    if(n %2 == 0):
        print("even number")
    else:
        print("odd number")
numbers(25)
print("--"*5)
    
