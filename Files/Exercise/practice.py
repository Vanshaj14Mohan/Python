#to replace a particular word in a file
with open("files/exercise/practice.txt", "r") as f:
    data=f.read()

newdata=data.replace("Java", "Python")
print(newdata)

with open("files/exercise/practice.txt", "w") as f:
    f.write(newdata)

#to find a paticular word in the file
word="learning"
with open("files/exercise/practice.txt", "r") as f:
    data=f.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("not found")