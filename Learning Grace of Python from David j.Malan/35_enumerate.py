
def dicCom3():
    studnets = ["harry", "ron", "hermione", "ginevra"]

    for i in range(len(studnets)):
        print(i+1, studnets[i])

# but there is a better way to do this
# using enumerate function


def dicCom4():
    studnets = ["harry", "ron", "hermione", "ginevra"]

    for i, studnet in enumerate(studnets):
        print(i+1, studnet)


# generators
# generators are iterators
def gen():
    n = int(input("Whats n? "))
    for i in range(n):
        print("🐑"*i)
        # if we try to print 1M sheep it will run out of storage
        # so we can use yeild. yeild is a generator


def gen2(n):
    for i in range(n):
        yield "🐑"*i


def gen1():
    n = int(input("Whats n? "))
    for s in gen2(n):
        print(s)

#iterators
