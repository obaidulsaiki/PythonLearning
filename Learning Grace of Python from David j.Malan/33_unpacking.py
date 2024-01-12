
def unpack():
    first, last = input("whats your name? ").split(" ")
    print(f"hello {first} {last}")


def total(galleons, sickles, knuts):
    return galleons*17*29 + sickles*29 + knuts

    """
    :FOR LIST
    coins = [1, 2, 3]
    print(total(coins[0], coins[1], coins[2]), "knuts is your total")
    to make this like more pythonic we can use unpacking
    *coins will unpack the list and pass the values to the function
    print(total(*coins), "knuts is your total")
    """

    """
    :FOR DICTIONARY
    coins = {"galleons": 1, "sickles": 2, "knuts": 3}
    print(total(coins["galleons"],
    coins["sickles"], coins["knuts"]), "knuts is your total")
    # **coins will unpack the dictionary and pass the values to the function
    print(total(**coins), "knuts is your total")
    """

# *args and **kwargs
# *args will pack all the values in a tuple
# **kwargs will pack all the values in a dictionary


def variatic(*args, **kwargs):
    print(args)
    print(kwargs)


variatic(100, 50, 11, name="harry", age=20)
