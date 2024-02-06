#1-> Store following word meanings in a python dictionary.
random = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts and figures"]
}
print(random)

#2-> You are given a list of subjects for students. Assume one classroom is required for 1 subject,
#how many classrooms are needed for alll students.
subjects = {"python", "java", "C++", "C", "python", "java", "javascript"}
print(len(subjects))#5-> classrooms
print(subjects)

#3-> Wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary,
#and add by one.Use subject name as key and marks as value.
marks ={}

marks1 = int(input("enter maths marks:"))
marks.update({"maths": marks1})
marks2 = int(input("enter computer marks:"))
marks.update({"computer": marks2})
marks3 = int(input("enter science marks:"))
marks.update({"science": marks3})
print(marks)

#4-> Figure out a way to store 9 & 9.0 as separate values in the set.
#two solutions for this.
#1. storing one of them in string form.
set = {9, "9.0"} #using a string in set
print(set)
#2-> using built-in data types.
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)