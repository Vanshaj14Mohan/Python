# A file I/O syntax
f = open("E:\Python\Files\demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()