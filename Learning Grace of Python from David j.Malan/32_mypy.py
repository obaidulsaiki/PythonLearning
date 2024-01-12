import argparse


def meow(n: int):
    for _ in range(n):
        print('meow')


# number: int = int(input('Enter a number: '))
# if pass the number varibale there will be error because it is a string
# so we should run the program with mypy to check the type of the variable and use typehints
# meow(number)
# when a function has no return it will return None
# if we want to return nothing we can use None
# we use typehints to tell the function what type of variable it should return


def meow2(n: int) -> None:
    for _ in range(n):
        return 'meow meow '*n


# N: str = meow2(number)
# print(N, end='')
# doctstring notation
# it is a way to document our code
"""we use triple quotes to write a docstring
    def meow2(n: int) -> None:
    """
# argparse - it is a module that helps us to parse the arguments that we pass to the program


def arg1():
    import sys
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == '-n':
        print("meow meow "*int(sys.argv[2]))
    else:
        print("wrong parser")


# arg1()
# argparse - argument parser
parser = argparse.ArgumentParser(description="meow like a cat")
"""
parser.add_argument('-n', help="number of meows", type=int)
here -n is the argument that we pass to the program
help - it will show the help message
type - it will tell the type of the argument
defualt - it will set the default value of the argument
"""
parser.add_argument('-n', help="number of meows", type=int, default=1)
args = parser.parse_args()
for _ in range(int(args.n)):
    print('meow meow')
# python 32_mypy.py -n 5
# -h - help
# -n - number
