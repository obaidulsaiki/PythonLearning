import random


class SortingHate:
    # def __init__(self):  # we dont need to pass self here as it is not called by the user
    # houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # @classmethod  # class method decorator
    # def sort(cls, name):  # we dont need to pass self as init is not called by the user
    # we cannot use self.name here
    # print(f"{name} is in {random.choice(cls.houses)}")
    # house = random.choice(self.houses)
    # print(f"{self.name} is in {house}")
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"

    @classmethod
    def get_student(cls):
        name = input("Enter the name of the student: ")
        house = input("Enter the house of the student: ")

        return cls(name, house)


def main():
    # hat = SortingHate() after using class method decorator we dont need to create an object
    # to call the SortingHate.sort("harry")  # kind of encapsulation
    student = SortingHate.get_student()
    print(student)


main()
# there is also staticmethod decorator
