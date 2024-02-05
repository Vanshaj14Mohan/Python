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
std.add(2)
std.add(5)
std.add("nice")
std.add(1)
print(std)