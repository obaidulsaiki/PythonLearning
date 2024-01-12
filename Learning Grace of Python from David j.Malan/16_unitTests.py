from userDefinedLibrery import hello, goodbye
from userDefinedLibrery import square


def main():
   # test_square()
   # test_squareOp()
   # test_squareOp1()
    squaretest()
    testhello()


def test_square():
    if (square(2) == 4):
        print("Test passed for 2")
    elif (square(3) == 9):
        print("Test passed for 3")
    else:
        print("not a valid result")

# but there is an optimize way to do this
# assert is a keyword in python


def test_squareOp():
    assert square(2) == 4
    assert square(3) == 9


# if the condition is true then it will not print anything
# but if the condition is false then it will print AssertionError
# to deal with the assertion error we can use try and except block
def test_squareOp1():
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed for 2")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed for 2")
    try:
        assert square(4) == 16
    except AssertionError:
        print("Test failed for 4")
# this is also very long way to test the function
# so we can use unittest module to test the function
# unittest module is a built in module in python
# but we can use pytest module to test the function
# pytest module is not a built in module in python
# we have to install it first
# pytest is simplier than the unittest module


def squaretest():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

# pytest will run all the test cases and will show the result
# if all the test cases are passed then it will show the result as 100% passed
# if any of the test case is failed then it will show the result as 100% failed
# it wont check every test case if any of the test case is failed
# to do that we can make those statements as a function individually
# testing string


def testhello():
    assert hello("John") == "Hello John"


if __name__ == "__main__":
    main()
# if we want to make folder and test all file on the folder we have to create a file name as __init__.py
# then we have to run pytest
# pytest will run all the test cases and will show the result