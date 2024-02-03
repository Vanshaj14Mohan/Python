#1: Wap to ask user to enter names of their 3 favorite movies & store them in a list.
# movie1 = input("enter movie one")
# movie2 = input("enter movie two")
# movie3 = input("enter movie three")

# list =[]
# list.append(movie1)
# list.append(movie2)
# list.append(movie3)
# print(list)

# #Another way -> to directly append it

# movies =[]
# movies.append(input("enter first movie"))
# movies.append(input("enter second movie"))
# movies.append(input("enter third movie"))
# print(movies)

#2: Wap to check if a list contains a palindrome of elements.

list1 = [1,2,3]
list2 = [5,2,5]

listcopy = list1.copy()
listcopy.reverse()

if(list1 == listcopy):
    print("Palindrome element")
else:
    print("Not a palindrome") 

list2copy = list2.copy()
list2copy.reverse()

if(list2 == list2copy):
    print("Palindrome number")
else:
    print("Not a palindrome number")

#3: Wap to count the number of students wit the "A" grade in the following tuple

random = ("C","D", "A", "A", "B", "B", "A")
print(random.count("A")) #3

#4: Store above values in a list and sort them from A to D
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)#["A", "A", "A", "B", "B", "C", "D"]