# properties of a class
# properties are function that modifies the attributes of a class
class Student:
    def __init__(self):
        self.name = "Harry"  # if we have this type of variable, we cannot use getter and setter
        # to use getter and setter, we need to use self._name
        self.house = "Gryffindor"

    def __str__(self):
        return f"{self.name} is in {self.house}"
# getter - to get the value of the attribute
# to use getter, we need to use the decorator @property

    @property
    def house(self):
        return self._house
    # setter - to set the value of the attribute
    # to use setter, we need to use the decorator @function_name.setter

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid House")
        self._house = house  # _house is a private variable
        # using setter we are protecting the value of the variable from being changed by the user

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in ["Harry", "Ron", "Hermione"]:
            raise ValueError("Invalid name")
        self._name = name


def main():
    student = Student()
    student.house = "Slytherin"  # student.house = means calling the setter function
    # we can use studnet._house = "outside house" to change the value of the variable
    # _ means private variable dont touch it but we can change it either way
    print(student)


# int,str,list,dict all are classes to know that we can use type() function
main()
