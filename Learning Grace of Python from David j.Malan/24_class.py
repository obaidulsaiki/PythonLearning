def main():
    student = get_Student()
    # print(student) it will print <__main__.Student object at 0x0000017ECB8065A0>
    # so we have to use__str__ method to print the object
    # there are many times of methods in python
    # __init__ is a method which is called instance method and it is called when an object is created
    # __str__ is a method which is called when we try to print the object
    # __repr__ is a method which is called when we try to print the object
    # __eq__ is a method which is called when we try to compare two objects
    # __hash__ is a method which is called when we try to hash the object
    # __bool__ is a method which is called when we try to convert the object to boolean
    # __len__ is a method which is called when we try to get the length of the object
    # __getitem__ is a method which is called when we try to get the item of the object
    # __setitem__ is a method which is called when we try to set the item of the object
    # __delitem__ is a method which is called when we try to delete the item of the object
    # __iter__ is a method which is called when we try to iterate the object
    # __contains__ is a method which is called when we try to check if the object contains the item
    # we can also use dot notation and change the name of the variable of student
    # student.name = "Ron" meaning we can change the value of the variable

    print(student)
    print(student.name)
    print(student.house)
    print(student.charm())


class Student:
    # __init__ is a method which is called instance method and it is called when an object is created
    # self is a reference to the current instance of the class
    def __init__(self, name, house, patronus):
        # what if there is case where a customer dont entered there name
        # we can use raise exception to handle this case
        # we can also use try and except block to handle this case
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is in {self.house}"

    def charm(self):  # userdefined method
        match self.patronus:
            case "stag":
                return "🐴" + " expecto patronum"  # to get horse i have to click windows + ;
            case "otter":
                return "🐸" + " expecto iscular"
            case _:
                return "die"


def get_Student():
    # student = Student()  # creating object of class Student
    # student.name = "Harry"  # attributes of class Student
    # student.age = 20
    # student.marks = 90
    name = "Harry"
    house = "Gryffindor"
    # creating function of class Student also known as method
    # constructor in python means creating object of class
    student = Student(name, house, "stag")
    return student


if __name__ == "__main__":
    main()
