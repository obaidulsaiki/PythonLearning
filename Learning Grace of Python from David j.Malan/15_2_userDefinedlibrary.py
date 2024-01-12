import sys
from userDefinedLibrery import hello, goodbye
if (len(sys.argv) == 2):
    search_term = sys.argv[1]
else:
    print("Please enter the search term")
    sys.exit()
# here this is a problem as the argument is not passed to the function
hello(search_term) #now it will give the output davd from the userDefinedLibrery.py
