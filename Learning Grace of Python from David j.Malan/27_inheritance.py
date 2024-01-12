
# we should not copy paste the code from the parent class to the child class
# we should use inheritance
class wizerd:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name


class student(wizerd):
    def __init__(self, name, house):
        # super() reference to the parent class and we can pass the name in wizard class
        super().__init__(name)
        self.house = house


class professor(wizerd):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = wizerd("Merlin")
student = student("Harry", "Gryffindor")
professor = professor("Snape", "Potions")
print(student.name, student.house)
print(professor.name, professor.subject)
print(wizard.name)
