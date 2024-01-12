def main():
    n = getnumber()
    hellow(n)


def getnumber():
    while True:
        n = int(input("Enter a positive integer: "))
        if n >= 0:
            return n
        else:
            print("The number must be positive.")


def hellow(n):
    for _ in range(n):
        print("Hello")


main()
