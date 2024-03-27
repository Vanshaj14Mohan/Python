#to replace a particular word in a file
with open("files/exercise/practice.txt", "r") as f:
    data=f.read()

newdata=data.replace("Java", "Python")
print(newdata)

with open("files/exercise/practice.txt", "w") as f:
     f.write(newdata)

#to find a paticular word in the file
def check_for_words():
        word="learning"
        with open("files/exercise/practice.txt", "r") as f:
            data=f.read()
            if(data.find(word)!= -1):
                print("found")
            else:
                print("not found")
 
check_for_words()

#to find in which line of the file does the word learning occurs first 