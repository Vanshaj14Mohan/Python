#DICTIONARY -> They are used to store data values in key:value pairs.
#properties ->unordered, mutable(changeable) & dont't allow duplicate keys.
dict1 ={
    "key": "value",
    "name": "Vanshaj",
    "hobby": "coding",
    "age": 21,
    "marks": 92.5,
    "is_adult": True
}
print(dict1)
print(type(dict1)) #dict

#We can even store list and tuple in a dictionary. But we can't use them in place of keys only tuple coz immutable
subject ={
    "Subjects": ["Maths", "English", "Hindi", "Computer"],
    "Topics": ("List", "Tuple", "Dictionary", "Set")
}
print(subject)
print(type(subject)) #dict

#to access values in dictionary
print(dict1["key"]) #value
print(dict1["name"])#Vanshaj
print(dict1["age"])#21

#Changing elements
dict1["marks"] =92.7,
print(dict1)

#Adding elements
dict1["skills"] = "Frontend developer",
print(dict1)

#creating a null dict and adding elements in it.
null_dict ={}
print(type(null_dict))
null_dict["name"] ="null"
null_dict["values"] ="real"
print(null_dict)

#Nested dictionaries
#value -> dictionary
student = {
    "name": "Alex",
    "subjects": {
        "Maths": 91,
        "Computer": 95,
        "Science": 90
    }
}
print(student)
print(student["subjects"])#For all subjects
print(len(student))#2

#Now for particular subjects
print(student["subjects"]["Maths"])#91
print(student["subjects"]["Computer"])#95
print(student["subjects"]["Science"])#90

#trick
#typecasting into list
print(list(student.keys()))#now it will be converted into list.
print(len(list(student.keys())))#2

#Dictionary methods
#1-> dic.key() ->returns all the keys in the dictionary.
print(student.keys()) #['name','subjects']
print(len(student.keys()))#2

#2-> dic.values() ->returns all the values in the dictionary.
print(student.values())#Alex, {Maths: 91, Computer: 95, Science: 90}
print(len(student.values()))#2

#3-> dic.items() ->returns all (key,val) pairs as tuples.
print(student.items())#returns all itmes in a tuple.
print(len(student.items()))#2
#we can typecast it too.
print(list(student.items())) #give result in a list

#4-> dic.get("key") -> returns the key according to value
print(student.get("name"))#Alex, used most by coders coz if we pass wong key it does'nt show error instead gives none.
print(student.get("subjects"))#{"Maths": 91, "Computer": 95, "Science": 90}

#5-> dic.update() -> inserts the specified items to the dictionary.
#suppose we wanna city city  in student dictionary.
print(student.update({"city": "Lucknow"})) #city will be shown in student dict
print(student)
#another way,
#we can pass new k:v pairs through a variable
gender = {"gender": "Male"}
student.update(gender)
print(student)#gender key & value will be shown now