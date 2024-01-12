# regex = regular expression
# regex is a language unto itself
# regex is supported in python and many other languages
# regex is a powerful tool for matching patterns in text
# solving validation problems:
# email addresses, phone numbers, zip codes, etc.
# white space from after the sentance and before the sentance
email = input("Enter your email address: ").strip()


def codv1():
    if '@' in email and '.' in email:
        print("Valid email address")
    else:
        print("Invalid email address")
    # the above code is not very robust
    # it does not check for multiple '@' signs
    # it does not check for a '.' after the '@' sign
    # to improve this we also have to check . after @


def codv2():
    username, domain = email.split('@')
    if username and '.' in domain:
        print("valid")
    else:
        print("invalid")


def codv3():
    username, domain = email.split('@')
    patern = ".edu", ".com", ".org", ".net"
    # to mass many argument through endswith we use variable
    # but when a single argument is passed we can use string
    if username and domain.endswith(patern):
        print("valid")
    else:
        print("invalid")


# for regular expression we have to import re module
# re module is used to match patterns in text
# re we can define pattern and search for it
# re.search(pattern, string, flags=0)
# pattern  = the regular expression to be matched
# string = the string which would be searched to match the pattern anywhere in the string
def codv4():
    import re
    if re.search("@", email):
        print("valid")
    else:
        print("invalid")
        # this code is not very useful as it only checks for @ sign
# . any character except new line
# * 0 or more times
# + 1 or more times
# ? 0 or 1 time
# {m} m number of times
# {m,n} m to n times


def codv5():
    import re
    if re.search(".*@.*", email):  # check all valid if it contains @
        # if re.search(".*@.+", email) if there is word after@ and before @ its valid
        # there is except case in the last node
        print("valid")
    else:
        print("invalid")


def codv6():
    import re
    # if re.search(".*@.+.edu", email): this is wrong because in regex . is for any character new line
    # \ is special sequence in regex \. meaning . is not for any character but for .
    if re.search(r".*@.+\.edu", email):
        # we also have to use r before the string to make it raw string
        # row string should be used in all regex
        print("valid")
    else:
        print("invalid")


# ^ start of string
# $ end of string
# the code in the upper section is not very useful for a string line
# to make it more useful we have to use ^ and $
def codv7():
    import re
    # if re.search(".*@.+.edu", email): this is wrong because in regex . is for any character new line
    # \ is special sequence in regex \. meaning . is not for any character but for .
    if re.search(r"^.+@.+\.edu$", email):
        # we also have to use r before the string to make it raw string
        # row string should be used in all regex
        print("valid")
    else:
        print("invalid")
# there is a case if there is @ multiple time then that thing will be invalid
# [] used to indicate a set of characters
# [a-z] lower case letters
# [A-Z] upper case letters
# [0-9] digits
# [^] complement of set - evething that is not in the set


def codv8():
    import re
    if re.search(r"^[^@]+@.[^@]+\.edu$", email):
        # [^@] means everything except @
        # + means one or more times of the thing before it
        print("valid")
    else:
        print("invalid")

# to improve the code furthur


def codv9():
    import re
    if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
        # [^@] means everything except @
        # + means one or more times of the thing before it
        print("valid")
    else:
        print("invalid")
# we can improve it furthur by using \w


def codv10():
    import re
    if re.search(r"^\w+@\w+\.edu$", email):
        # \w means any alphanumeric characters [a-zA-Z0-9_]
        # \w+ means one or more times of alphanumeric characters
        print("valid")
    else:
        print("invalid")


# \d means any digit [0-9]
# \d+ means one or more times of digits
# \s means any white space character
# \s+ means one or more times of white space character
# \S means any non white space character
# \S+ means one or more times of non white space character
# \b means word boundary
# \B means non word boundary
# \W means non word character
def codv11():
    import re
    if re.search(r"^\w+@\w+\.(edu|com|net)$", email):
        print("valid")
    else:
        print("invalid")
# flag = re.IGNORECASE, re.MULTILINE, re.DOTALL
# re.IGNORECASE = ignore case
# re.MULTILINE = ^ and $ will match the start and end of each line
# re.DOTALL = . will match any character including new line
# to make it more robust we can use flag


def codv12():
    import re
    if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|net)$", email, re.IGNORECASE):
        print("valid")
    else:
        print("invalid")


# regular expression of email validate is very complex
# re.match() = checks for a match only at the beginning of the string
# re.fullmatch() = checks for a match only if the whole string matches
# re.findall() = returns a list of all matches
# re.finditer() = returns an iterator of all matches
codv12()
