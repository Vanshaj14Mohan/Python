#Creating a tuple

tup =(1,2,3,4)
print(type(tup)) #Tuple

#we can print it's indexes too
print(tup[0], tup[1], tup[2], tup[3]) #[1,2,3,4]

#slicing in tuples
print(tup[0:3])#(1,2,3)
print(tup[1:3])#(2,3)
print(tup[2:4])#(3,4)
print(tup[0:4])#(1,2,3,4)
print(tup[:4])#(1,2,3,4)

#tuple methods
print(tup.index(2))#1
#returns index of first occurrence
print(tup.index(1), tup.index(3), tup.index(4)) #0,2,3
print(tup.count(2))#1
print(tup.count(4))#1
#counts total occurrences

tup2 =(1,2,3,2,3,5,5,5,7)
print(tup2.count(2))#2
print(tup2.count(3))#2
print(tup2.count(5))#3
