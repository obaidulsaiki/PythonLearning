# there are 4 concept of oop
# 1. Abstraction - hiding the complexity or detailes and showing only the essential features of the object
# 2. Encapsulation - binding the data and the functions that manipulates them
# 3. Inheritance - a class can inherit attributes and methods from another class
# 4. Polymorphism - the ability to take various forms

# -------abstraction----------------
def main():
    # name, horsepower = get_name(), get_horsepower()
   # name, horsepower = getcar() we can get the value this way or the way below
    car = getcar()
    if car["name"] == "subaru":
        car["horsepower"] = 300
    print(f"{car['name']} has {car['horsepower']}hp")


def getcar():
    # tuple of 2 elements (name, horsepower)
    # tuple is like a list but its immutable(unable to be changed) it will through an TypeError if we try to change it
    # return "subaru", "250"
    # but if we use a list we can change the value of the list
    # return ["subaru", 250]
    # but we can use dictionary to make it more readable
    # by using dictionary we can access the value by using the key
    # return {"name": input("name: "), "horsepower": input("horsepower: ")}
    return {"name": "suburu", "horsepower": "250"}

if __name__ == "__main__":  # this is added for a case for example if we want to access from another file
    # the main funciton wont be call all the time

    main()
