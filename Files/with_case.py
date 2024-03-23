with open("E:\Python\Files\with.txt", "r") as f:
    data= f.read()
    print(data)

#f.close(), not compulsory with, with Syntax, coz with automatically closes file for us.
    
#for "w" case:    
with open("E:\Python\Files\with.txt", "w") as f:
    f.write("New data for more test.")