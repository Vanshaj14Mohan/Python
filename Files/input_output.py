# A file I/O syntax
f = open("E:\Python\Files\demo.txt", "r")
#data = f.read() #read entire file
#data = f.read(7) starting 7 words of the file
line = f.readline() #reads one line at a time
print(line)
line2 = f.readline()
print(line2)
#print(data)
#print(type(data))
f.close() #to close file