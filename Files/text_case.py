#Now to combine our notes.
#"r+" file will not truncate
#"w+" file will truncate
# f =open("E:\Python\Files\sample.txt", "r+") #overwrites the text in the beginning
# f.write("abcd")
# print(f.read())
# f.close()

#same for "w+"
# f =open("E:\Python\Files\sample.txt", "w+") #overwrites the text in the beginning
# #f.write("abcd")
# print(f.read()) #will print nothing, coz it's truncated
# #but we can write after that
# f.write("abcd")
# f.close()

#same for "a+"
f =open("E:\Python\Files\sample.txt", "a+") #overwrites the text in the beginning
print(f.read()) #will print nothing,
f.write("abcd") #will append data in the last
f.close() 
