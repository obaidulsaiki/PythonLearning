# map
# a program for yelling
def main():
    # yell("this is me")
    ...


def yel1(phrase):
    print(phrase.upper())


def yel2(*words):
    upercase = []
    for word in words:
        upercase.append(word.upper())
    # * unpacks the list it will print T H I S   I S   M E but we can use * words so that we can improve
    print(*upercase)


def yel3(*phrase):
    # using map
    uppercased_phrase = map(str.upper, phrase)  # map(function, iterable)
    print(*uppercased_phrase)

# list comphrehension


def yell(*words):
    uppercase = [word.upper() for word in words]
    print(*uppercase)


def listComprehension():
    student = [
        {"name": "harry", "house": "gryffindor"},
        {"name": "cho", "house": "gryffindor"},
        {"name": "draco", "house": "slytherin"},
    ]
    gryffindors = [
        std["name"] for std in student if std["house"] == "gryffindor"
    ]
    for gryffindor in sorted(gryffindors):
        print(gryffindor)
# filter function


def for_filter():
    student = [
        {"name": "harry", "house": "gryffindor"},
        {"name": "cho", "house": "gryffindor"},
        {"name": "draco", "house": "slytherin"},
    ]
    gryffindors = filter(lambda std: std["house"] == "gryffindor", student)
    for gryffindor in sorted(gryffindors, key=lambda std: std["name"]):
        print(gryffindor["name"])


# dictionary Comprehension
def dicCom():
    studnets = ["harry", "ron", "hermione", "ginevra"]

    gryffindor = []
    for studnet in studnets:
        gryffindor.append({"name": studnet, "House": "gryffindor"})
    print(gryffindor)


# we can improve it
def dicCom2():
    studnets = ["harry", "ron", "hermione", "ginevra"]

    gryffindorS = [{"name": studnet, "House": "gryffindor"}
                   for studnet in studnets]
    for gryffindor in gryffindorS:
        print(gryffindor)
# we also optimize it


def dicCom3():
    studnets = ["harry", "ron", "hermione", "ginevra"]

    for i in range(len(studnets)):
        print(i+1, studnets[i])


dicCom3()
if __name__ == "__main__":
    main()
