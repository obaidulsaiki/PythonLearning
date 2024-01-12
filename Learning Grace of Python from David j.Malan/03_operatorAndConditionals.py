# -------------------use of + , - , * , / , % , ** , //-------
# x = input("Enter the value of x: ") - 1
# y = input("Enter the value of y: ") - 2
# print(x+y) - 12
# if we use x+y it will produce 12 as output by doing concatenation
# print(int(x) + int(y)) will produce 3 as output
# using int() directly
x = 5
y = 3
print(x+y)  # Addition - 8
print(x-y)  # substraction - 2
print(x*y)  # multiplication - 15
print(x/y)  # division - 1.6666666666666667
print(x**2)  # power - 25
print(x//y)  # floor division - 1 || 5/3 = 1
print(x % y)  # modulus - remainder - 2
# ---conditional operator(>, >=, <, <=, ==, != )----------
# > greater than
# >= greater than or equal to
# < less than
# <= less than or equal to
# == equal to
#!= not equal to
# if else
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
if x != y:
    print("x is not equal to y")
else:
    print("NOTHING")
print("--------------")
# elif ( else if)
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
elif x != y:
    print("x is not equal to y")
else:
    print("NOTHING")
# or operator
if x < y or x > y:
    print("X and Y isn not equal")
else:
    print("X and Y is equal")

# program to assign grade in python
grade = int(input("Enter your grade: "))
if grade >= 90 and grade <= 100:
    print("A")

elif 80<= grade <= 90:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
#
