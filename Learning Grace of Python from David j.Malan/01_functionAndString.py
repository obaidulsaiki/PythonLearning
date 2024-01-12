# print funtion with argument - printing hello world
print("Hello world!")
# we use # for single comment and ''' '''  for double comment
# input function also takes argument itself so we can declare string in this input function
# input("arguments " )
# varibale declaration - variables are containers for storing data values,always expect string
# variable name should start with letter or underscore not number
variablename = input("Whats your name? ")
print("Hello " + variablename + "!")  # it takes no space
print("Hello", variablename, "!")  # it takes auto space
# here the syntex of print is print(value,sep,end="\n",file,flush)
print(variablename)
# print funtion takes auto newline so we have to remove end="\n" from the print function
print(variablename, end=" ")
print(variablename)
# string in python is str
# we can declare another way format string
print(f"Hello {variablename}!")  # f is format string
# functions of string
stringname = "   Hello world!"
print(stringname.upper())  # convet all uppercase function

print(stringname.lower())  # convert all lower function
# remove extra white spaces from before the word and after the word function
print(stringname.strip())
# capitalize first letter of the string
print(stringname.capitalize())
# title function capitalize first letter of every word
print(stringname.title())
# we can make a chain of funtion
print(stringname.strip().capitalize())
# we can also use like that
stringname1 = " new LANGUaGe".strip().title()
print(stringname1)
# split user name in first name and second name
split_name = input("What is your name? ").strip().title().split()
first, last = split_name
print(f"Hello {first}, {last}!")
