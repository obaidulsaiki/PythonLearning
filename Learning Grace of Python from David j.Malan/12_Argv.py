# sys module
# exit() which will exit the program
# argv() which will take the command line argument
# from the user's input
# command line argument - the argument that we pass when we run the program
# argv - argument vector
def sys_Learnin():
    import sys
    print("my name is ", sys.argv[1])
# sys.argv[0] - will print the location and name of the file
# if user dont enter anything in will give index error
# to avoid this we can use if statement or try


def optimized_Sys():
    import sys
    try:
        print("my name is ", sys.argv[1])
    except IndexError:
        print("to few argument")


def exitfunction():
    import sys
    # sys.exit() - will exit the program
    if (len(sys.argv)) != 2:
        sys.exit("to few argument")
    print("my name is ", sys.argv[1])


# exitfunction()
def MultipleArg():
    import sys
    if len(sys.argv) < 3:
        sys.exit("to few argument")
    for arg in sys.argv:
        print("I am the ext " + arg)


# MultipleArg()
# if we want to pass multiple argument we can use for loop
# but there is a problem as in the index 0 it will print the location of the file
# To remove this we can use slicing
# for arg in sys.argv[start:endlimit]:
def MultipleArg():
    import sys
    if len(sys.argv) < 3:
        sys.exit("to few argument")
    for arg in sys.argv[1:]:  # slicing starting from 1 index
        print("I am the ext " + arg)


MultipleArg()
