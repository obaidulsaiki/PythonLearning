# normally developers store information in a CSV file
# CSV file is comma separated values
# we can use csv module to read and write csv files

def outputingv7():
    with open("17_student.csv", "r") as file:
        for line in file:
            # print(line.strip().split(",")) this will generate list of list
            row = line.strip().split(",")
            firstname, lastname = row
            print(f"Hello {firstname} {lastname}")


def get_name(student):
    return student["firstname"]


def outputingv8():
    # sorting the information using dictionary
    students = []
    with open("17_student.csv", "r") as file:
        for line in file:
            student = {}
            student["firstname"], student["lastname"] = line.strip().split(",")
            students.append(student)
    for student in sorted(students, key=get_name):
        # we are using dictionary so we have to use key
        print(f"Hello {student['firstname']} {student['lastname']}")
        # we didnt use "" because we are using f string  and we are using dictionary so we have to use key

# lamda function is a function that we can use only once
# lamda is also known as anonymous function
# lamda function is used to sort the information in one line
# lamda syntax is lamda parameter: expression
# # in the upper section get_name is used only once so we can use lamda function


def outputingv9():
    students = []
    with open("17_student.csv", "r") as file:
        for line in file:
            student = {}
            student["firstname"], student["lastname"] = line.strip().split(",")
            students.append(student)
    for student in sorted(students, key=lambda student: student["firstname"]):
        # we are using dictionary so we have to use key
        print(f"Hello {student['firstname']} {student['lastname']}")

        # we didnt use "" because we are using f string  and we are using dictionary so we have to use key


# using CSV module
# we can use csv module to read and write csv files
import csv 

def outputingv10():
    students = []
    with open("17_student.csv", "r") as file:
        # reader is a function that will read the file for us and evalute it as csv file
        reader = csv.reader(file)
        # we can use next function to skip the first line
        # for row in reader:
        # students.append({"firstname":row[0], "lastname":row[1]})
        for name, home in reader:
            students.append({"firstname": name, "lastname": home})
    for student in sorted(students, key=lambda student: student["firstname"], reverse=True):
        print(f"Hello {student["firstname"]} from {student["lastname"]} ")
# we can see in a spreedshit that first row is different so to use it like that we are gonna use DictReader


def outputingv11():
    students = []
    with open("17_student.csv", "r") as file:
        reader = csv.DictReader(file)

        # Print the header row
        print(reader.fieldnames)

        for row in reader:
            students.append({"home": row["home"], "name": row["name"]})

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"Hello {student['home']} from {student['name']}")


outputingv11()
