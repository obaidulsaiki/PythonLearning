# how to dynamically print a #brick of maria games
# we can use for loop but it not going to be a good idea
def main():
    # print_Column_bricks(3)
   # printColumnBricks(3)
    # printRowBricks(4)
    square(3)


def print_Column_bricks(height):
    for i in range(height):
        print("#")
# we can implement it another way more readable


def printColumnBricks(height):
    print("#\n" * height, end="")


def printRowBricks(width):
    print("?" * width, end="")


def squares(height):
    # outer loop works for rows
    for i in range(height):
        # inner loop works for columns
        for j in range(height):
            print("#", end="")
        print()  # newline
# we can minimize the code by using multi-concatation


def square(height):
    # outer loop works for rows
    for i in range(height):
        print("#" * height)
main()
