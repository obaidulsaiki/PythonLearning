# user defined function with finding parity
def main():
    x = int(input("Enter a number: "))
    if iseven(x):
        print("Even")
    else:
        print("Odd")
    if optimized_iseven(x):
        print("Even")
    else:
        print("Odd")
def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def optimized_iseven(n):
    return n % 2 == 0
#main()
#keyword match
name = input("Enter your name: ")
match name: #match keyword
    case "Alice":
        print("Hello, Alice")
    case "Bob":
        print("Hello, Bob")
    case _:
        print("Hello, stranger")