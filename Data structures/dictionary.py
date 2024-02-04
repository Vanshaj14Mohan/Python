#DICTIONARY -> They are
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