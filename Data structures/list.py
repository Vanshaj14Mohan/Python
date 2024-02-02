#List data structure is a special data structure in python
#Some properties of list might seem same as string
#We can store elements of different types together(int, float, string.. etc)

# marks = [90.2, 95.5, 82.8, 80, 78.9, 95.1, 88.5, 92.0, 98]
# print(marks)
# print(type(marks)) #list
# print(marks[0], marks[1], marks[7], marks[5]) #90.2, 95.5, 92.0, 95.1
# print(len(marks)) #9 

# random = ["sam", "arthur", 90, 87.25]
# print(random[0], random[1], random[2], random[3]) #sam, arthur, 90, 87.25
# print(type(random)) #list
# print(len(random)) #4

#Key point:
#1-> List are mutable in python, whereas string in python is immutable
# key =["hello", "good", "morning"]
# key[2] ="night"
# print(key[2]) #night
# print(key)# "hello", "good", "night" -> a new list

#slicing is possible here too
# print(random[0:4]) #sam, arthur, 90, 87.25
# print(random[1:3]) #arthur, 90, 87.25
# print(random[0:3]) #sam, arthur, 90
# print(random[:3]) #same as above
# print(random[-4:-1])#sam, arthur, 90
# print(random[::-1]) #print reverse order of random

#list methods

list = [5, 2, 3]
list.append(4) #adds one element at the end
print(list) #[5,2,3,4]
list.sort() #sorts in ascending order
print(list) #[2,3,4,5]
list.sort(reverse=True) #sorts in descending order
print(list) #[5,4,3,2]
list.reverse() #reverses list
print(list) #[2,3,4,5]
list.insert(1,6) #insert element at given index
print(list) #[2,6,3,4,5]
list.pop(1) #removes value at given index
print(list)#[2,3,4,5]
list.remove(3) #removes the first occurence of given element
print(list) #[2,4,5]

#Sorting also applies on characters, strings in python
#sorting is based on characters here -> a>b>c>d....ascending, a<b<c<d..descending
list2 = ["mango", "litchi", "apple", "kiwi", "orange"]
list2.sort()#["apple", "kiwi", "litchi", "mango", "orange"]
print(list2)
list2.sort(reverse=True) #["orange", "mango", "litchi", "kiwi", "apple"]
print(list2)
list2.reverse()
print(list2)#["apple", "kiwi", "litchi", "mango", "orange"]
list2.insert(2, "banana")
print(list2)#["apple", "kiwi", "banana", "litchi", "mango", "orange"]
list2.pop(3)
print(list2) #["apple", "kiwi", "banana", "mango", "orange"]
list2.remove("mango")
print(list2)#["apple", "kiwi", "banana", "orange"]
