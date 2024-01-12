# list-----like array
# list is a collection of items
students = ["Raj", "Rahul", "Ravi"]  # list of 3 string
print(students)  # here it prints all in the type of list
# but not value, to print value
print(students[0])  # prints Raj
print(students[1])  # prints Rahul
print(students[2])  # prints Ravi
# but for bigger number it will be hard to print so we use for loop
for student in students:
    # student is a variable which is already initialized in forloop
    print(student)
# if we want to iterate through the list
# print the index of the list
for i in range(len(students)):
    # len(students) gives the length of the list
    print(i, students[i])
