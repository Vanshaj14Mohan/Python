#List data structure is a special data structure in python
#Some properties of list might seem same as string
#We can store elements of different types together(int, float, string.. etc)

marks = [90.2, 95.5, 82.8, 80, 78.9, 95.1, 88.5, 92.0, 98]
print(marks)
print(type(marks)) #list
print(marks[0], marks[1], marks[7], marks[5]) #90.2, 95.5, 92.0, 95.1
print(len(marks)) #9 

random = ["sam", "arthur", 90, 87.25]
print(random[0], random[1], random[2], random[3]) #sam, arthur, 90, 87.25
print(type(random)) #list
print(len(random)) #4

#Key point:
#1-> List are mutable in python, whereas string in python is immutable
key =["hello", "good", "morning"]
key[2] ="night"
print(key[2]) #night
print(key)# "hello", "good", "night" -> a new list

#slicing is possible here too
print(random[0:4]) #sam, arthur, 90, 87.25
print(random[1:3]) #arthur, 90, 87.25
print(random[0:3]) #sam, arthur, 90
print(random[:3]) #same as above
print(random[-4:-1])#sam, arthur, 90
print(random[::-1]) #print reverse order of random

#list methods