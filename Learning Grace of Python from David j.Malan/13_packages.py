# packages in python is a way to structure python's module namespace by using "dotted module names"
# A directory must contain a file named __init__.py in order for python to consider it as a package.
# function()
# https://pypi.org/ - python package index
# cowsay - python package
# pip is package manager for python packages
# pip install cowsay
def forCowsayPack():
    import cowsay
    import sys
    if len(sys.argv) == 2:
        cowsay.cow("ANs me: " + sys.argv[1])
# print a cow saying hello

# forCowsayPack()


def forCowsayPack():
    import cowsay
    import sys
    if len(sys.argv) == 2:
        cowsay.trex("ANs me: " + sys.argv[1])
# print a trex saying hello


forCowsayPack()
