# set is typically a collection of unique value
# set is unordered
# filer out duplicate value
student = [
    {
        "name": "ron",
        "House": "Gryffindor"
    },
    {
        "name": "Harry",
        "House": "Gryffindor",
    },
    {
        "name": "Draco",
        "House": "Slytherin",
    },
    {
        "name": "Cho",
        "House": "Ravenclaw",
    }]


def normalway():
    House = []
    for student in student:
        if student["House"] not in House:
            House.append(student["House"])
    for house in sorted(House):
        print(house)


# aside from not using the condition we can just use set
houses = set()
for student in student:
    houses.add(student["House"])
for house in sorted(houses):
    print(house)
