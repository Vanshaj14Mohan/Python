# A file I/O syntax
#f = open("E:\Python\Files\demo.txt", "r")
#data = f.read() #read entire file
#data = f.read(7) starting 7 words of the file
# line = f.readline() #reads one line at a time
# print(line)
# line2 = f.readline()
# print(line2)
#print(data)
#print(type(data))
# f.close() to close file

#Now how to write in a file.
#2 ways to implement this
#1-> in "w" mode ie-> overwrite mode
#2-> in "a" mode ie-> in append mode
#f= open("E:\Python\Files\demo.txt", "w") #for write
#f.write("A basic start to file input/output operations in python") #replaces all data in demo.txt with new data
#2 way 
f=open("E:\Python\Files\demo.txt", "a") #to append data in the last
f.write("\n to append data we use a command in the last") #\n to bring it in new line
f.close()

#Note -> if we want to create a file which does'nt exist
#f=open("Sample.txt", "w") or f=open("Sample.txt", "a") both "w" & "a" will create a new file for us.