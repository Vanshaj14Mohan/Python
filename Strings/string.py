#Escape sequence characters.
str1 = "This is a string.\nWe are creating in python." #\n => Next line
print(str1)
#Or
str2 = "This is string two.\tWe are creating in python." #\t => Tab space between two sentences
print(str2)

#Now Basic operations on strings in python
#1:Concatenation
str3 ="Python"
str4 ="Language"
print(str3+" "+str4) #Python language
#or
strx =str3+str4
print(strx)#PythonLanguage(without spaces)

#2: length of an string => len(str)
print(len(str3))#6
print(len(str4))#8

#3: Indexing in strings 
str = "Code right"
print(str[0], str[2], str[4], str[7], str[8])#C,d, ,g,h

#4: Slicing in python
stry="Bootstrap"
print(stry[0:3], stry[3:5], stry[5:8], stry[:5], stry[0:], stry[0:len(stry)])#Boo, ts, tra, Boots, Bootstrap, Bootstrap
#Both str[0:] & stry[0:len(stry)] => will give same output

#Special case, : Negative indexing in python
print(stry[-1])#p
print(stry[-5:-2])#str
print(stry[-7:-4])#ots
print(stry[::-1])#partstooB, String reversed

#5: Functions in strings
x = "I am a coder"
print(x.endswith("er")) #Returns true if x endswith er or else false: Returns true in this case
print(x.endswith("am")) #False
print(x.capitalize())#Returns the first word of sentence as capital, It's already capital in our example
print(x.replace("am","was"))#Replaces old values with new ones.
x = "I am good at python"
print(x.replace("python", "javascript"))
print(x)
print(x.find("d"))#Returns first index of first occurence, ie=> 8, d position
print(x.find("g",)) #5
print(x.find("h"))#16
print(x.count("o"))#3 #Counts the number of occurence in a substring ie,how many times that number comes in a given string
print(x.count("a"))#2
print(x.count("python"))#1
