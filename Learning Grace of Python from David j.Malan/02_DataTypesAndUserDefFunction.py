# types of data
# int    - integer -infinty to +infinity
number = 1920
print(number)
# float  - floating point number - 1.0, 2.0, 3.0
print(1.0)
# round function round(variablename, decimal places)
X = 17.876
y = 178761212
print(round(X))  # will round off the value of X to nearest integer
print(round(X, 1))  # will round off the value of X to 1 floating place
print(round(X, 2))  # will round off the value of X to 2 floating place
print(f"{y:,}")  # will add comma to the number in each 3 digit from the right
print(f"{X:.2f}")  # it will print upto 2 floating point number after decimal

# str    - string - "hello", "world" default data type of python
# bool   - boolean - True, False
print(True)
# ----- later -----
# list   - list of items - [1, 2, 3, 4]
# dict   - dictionary - {"key": "value"}
# tuple  - tuple - (1, 2, 3, 4)
# set    - set - {1, 2, 3, 4}
# None   - NoneType - None
# complex - complex number - 1 + 2j

# ---------- user defined funtion ------------
# to use userdefined funtion we need def(define) keyword
# the define function should be at the top


def myfunction():
    print("Hello World")


name = "Rahul"
myfunction()
print(name)
# using parameter in function


def myfunction(name):
    print(f"Hello World to {name}")


name = "Rahul"
myfunction(name)
# assigning default value to parameter


def myfunction(name="Rahul"):
    print(f"Hello World to {name}")


myfunction()
lols = "dravid"
myfunction(lols)
# return type function - it will return the value to the function call


def myfunction(name):
    return 44


x = 10
newX = myfunction(x)
print(newX)
