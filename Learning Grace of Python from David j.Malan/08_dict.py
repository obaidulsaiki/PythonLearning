# (dict) dictionary is a collection which is unordered
# changeable and indexed. No duplicate members.
students = {
    # "key": "value"
    "name": "John",
    "age": 25,
    "courses": "Maths"
    # here by calling name we will get john name
}
# print(students) - it will only print the dictionary
print(students["age"])
print(students["name"])
print(students["courses"])
# this is impossible if we use 100 of variable
for key in students:
    print(key, " value:", students[key])  # this will print all the keys
# a list of dictionary
students = [
    {"Name": "John", "house": "Gryffindor", "patronus": "stag"},
    {"Name": "Harry", "house": "Gryffindor", "patronus": "otto"},
    {"Name": "harry", "house": "gryffindor", "patronus": None}
]
# python has build in keyword None which means nothing
for student in students:
    print(student["Name"], student["house"], student["patronus"], sep=",")
