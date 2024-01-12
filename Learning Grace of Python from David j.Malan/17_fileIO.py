# using file i/o to read and write files
# file = open("filename.txt", "r") # r is for read
# file = open("filename.txt", "w") # w is for write and it will overwrite the file
# file = open("filename.txt", "a") # a is for append and it will add the file
# file = open("filename.txt", "r+") # r+ is for read and write
# file = open("filename.txt", "w+") # w+ is for write and read
import csv


def outputingv1():
    names = []
    for _ in range(5):
        names.append(input("Enter your name: "))
        # if the file containes many input this way we have to write many lines
    for name in sorted(names):
        print(f"Hello {name}")
# to information the file we have to use with open


def outputingv2():
    file = open("17_output.txt", "a")
    names = []
    for _ in range(5):
        names.append(input())
        # if the file containes many input this way we have to write many lines
    for name in sorted(names):
        # it will give input in one line "makinakisakisaosaoi"
        # so we have add "\n" to make it in new line
        file.write(name+"\n")

    file.close()  # it is important to close the file
    # but sometimes we forgot to close the file so we can use with open
    # with open("17_output.txt", "a") as file:


def outputingv3():
    with open("17_input.txt", "r") as file:
        names = file.readlines()  # file.readlines() will give us list of lines
        # names.rstrp() will remove the "\n" from the list
        for name in names:
            print(f"Hello {name.rstrip()}")  # rstrip() will remove the "\n"


def outputingv4():
    names = []
    with open("17_input.txt", "r") as file:
        for name in file:
            names.append(name.rstrip())

    for name in sorted(names):
        print(f"Hello {name}")
        # we can sort it more easily by using sorted(file, key=len)


def outputingv5():
    with open("17_input.txt", "r") as file:
        for name in sorted(file):
            print(f"Hello, {name.rstrip()}")


def outputingv6():
    names = []
    with open("17_input.txt", "r") as file:
        names = sorted(name.strip() for name in file)
    with open("17_output.txt", "w") as file:
        for name in names:
            print(f"Hello, {name}", file=file)


# outputingv6()
# sorted(file, key=len, reverse = false) will sort the file by length
# to sort descending we have to use reverse = true
# sorted(file, key=str.lower) will sort the file by lower case
