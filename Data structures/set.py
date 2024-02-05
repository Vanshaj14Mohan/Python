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
#1: adding elements in set
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

#removing elements from set
std.remove(5)
std.remove(9)
print(std)#will print without 5 and 9 in it.

#to clear a set