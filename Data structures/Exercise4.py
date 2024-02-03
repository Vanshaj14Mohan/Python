#1: Wap to ask user to enter names of their 3 favorite movies & store them in a list.
movie1 = input("enter movie one")
movie2 = input("enter movie two")
movie3 = input("enter movie three")

list =[]
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)

#Another way -> to directly append it

movies =[]
movies.append(input("enter first movie"))
movies.append(input("enter second movie"))
movies.append(input("enter third movie"))
print(movies)

#2: Wap to check if a list contains a plaindrome of elements.