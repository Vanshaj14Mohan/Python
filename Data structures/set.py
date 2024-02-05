#Set is the collection of unordered items.
#Each element in the set must be unique and immutable.

nums = {1,2,3,4,2, "hello", "world", "world"}
print(nums)#will ignore duplicate values.
print(type(nums))#<class 'set'>
print(len(nums))#6, will also ignore duplicate itmes.

#creating an empty set.
std = set()
print(type(std))

#Methods in sets
#1-> adding elements in set
std.add(2)
std.add(5)
#we can store different values in set too.
std.add("nice")
std.add(1)
std.add(4)
std.add(8)
std.add(3)
std.add(9)
#we can pass tuple in it too, but we can't pass list and dict in it coz they are mutable
std.add((6,5,2))
print(std)

#2-> removing elements from set
std.remove(5)
std.remove(9)
print(std)#will print without 5 and 9 in it.

#3-> to clear a set ie. to make it empty.
set = set()
set.add(1)
set.add(2)
set.add("noon")
set.add("morning")
print(set)
print(len(set))#4
#now to clear it 
set.clear()
print(len(set))#0

#4-> to remove a random value
random ={"yup", "guys", 20, 90, 30, 80, "night", "dawn"}
print(random.pop())#removes any random value from set ie. from random

#Important methods.
#1-> set.union(), combines both set values and returns new.
set1 = {1,2,3,4}
set2 = {3,4,5,6,7}
print(set1.union(set2))#{1,2,3,4,5,6,7}, it returns a new set
#but does'nt change anything in the old sets.
print(set1)#{1,2,3,4}
print(set2)#{3,4,5,6,7}

#2-> set.intersection(), combines common values and returns new.
print(set1.intersection(set2))#{3,4}
#or
int1 = {1,2,3,4,5,7,8}
int2 ={4,5,2,3,7}
print(int1.intersection(int2))