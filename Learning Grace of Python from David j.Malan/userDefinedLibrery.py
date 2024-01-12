def main():
    x = int(input("Enter a number: "))
    print("X is squared", square(x))


def hello(name):
    # print("Hello " + name)
    # if we use pytest then we have to use return statement
    return f"Hello {name}"  


def goodbye(name):
    print("Goodbye " + name)


def square(x):
    return x * x


if __name__ == "__main__":  # __name__ is a special variable in Python.
    # It gets its value depending on how we execute the containing script.
    main()  # main funciton is called here in an conditional statement
    # if we run this script directly, __name__ will be equal to __main__.
