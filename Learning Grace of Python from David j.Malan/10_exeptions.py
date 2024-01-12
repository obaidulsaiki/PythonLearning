# how to fix the errors or handle exeptions
# syntax error, logical error, runtime error
# syntex error - when we use wrong syntax
# logical error - when we use wrong logic
# runtime error - when we use wrong input
# x = int(input("Enter a number: "))
# print(f"hello {x} is a number")
# if we enter a string it will give us an error
# this is value error - we can handle it by using try and except
def handle_valueerror():
    # we use function not to read this part of the code
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("invalid input")
# if we use print function for printing after
# this error it will not print and it will be name error
# to handle the name error we are gonna use else
    else:
        print("everything is fine")
        print(f"hello {x} is a number")
# we can make this code more efficient by using infinite loop
# and treating it like a function


def main():
    n = get_int("Enter a number: ")
    print(f"hello {n} is a number")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           # print("invalid input")
           # suppose if it is value error we want to pass
           # we can use pass
            pass


main()
# later raise
