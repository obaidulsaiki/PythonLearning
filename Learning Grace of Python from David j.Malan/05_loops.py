# introduction to loops
# ------ while loop--------
i = 0  # initialize
while i < 10:  # condition
    print(i, end=" ")  # print i meaning 0 to 9
    # if we want to print in one line we have to use end=" "
    # because in python print function takes default end="\n"
    # which means new line
    i += 1  # increment, there is no i++ in python
# for loop
for i in [0, 1, 2]:  # i will iterate 3 times because of 3 number
    print(i, end=" ")
# this is not a easy way because if we use 1m we have to input 1m number
# thats why range function is used
print()
for i in range(3):
    print(i)  # it will print 0,1,2
# if we dont want to name the variabe we can use _
for _ in range(3):
    print("Hello")  # we can use _ to print the range
# we can also use * to print a string multiple times
# print("Hello"*3)
print("Hello "*3)
# infinity loop
# while True:
# n = int(input("Enter a positive integer: "))
# if n < 0:break
