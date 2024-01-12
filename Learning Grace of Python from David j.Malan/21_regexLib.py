# there are complex regex libraries that can be used to make the code more efficient
# if we want to manually do it its really hard
# reformating user input
import re


def outputv1():
    name = input("Enter your name: ").strip()
    # print(f"Hello {name}")
    # if we want to make sure that the name is in the correct format
    # we can use regex
    if ',' in name:
        name1, name2 = name.split(',')  # 0 or 1 space if weput ? after space
        name = f"{name2} {name1}"
    print(f"Hello {name}")


def outputv2():
    # ^ start of string, $ end of string
    name = input("Enter your name: ").strip()
    match = re.search(r"^(.+), *(.+)$", name)
    print(match)
    if match:
        last, first = match.groups()  # groups() returns the whole string
        print(f"Hello {first} {last}")


def outputv3():
    # ^ start of string, $ end of string
    name = input("Enter your name: ").strip()
    match = re.search(r"^(.+), *(.+)$", name)
    # print(match)
    if match:
        # groups() returns the whole string
        name = match.group(1) + " " + match.group(2)
    print(f"Hello {name}")


def outputv4():
    name = input("Enter your name: ").strip()
    #if match := re.search(r"^(.+), *(.+)$", name): we cannot use this to use this type of things
    #we are going to use wallrice operator ":="
    if match := re.search(r"^(.+), *(.+)$", name):
        name = match.group(1) + " " + match.group(2)
    print(f"Hello {name}")


outputv4()
