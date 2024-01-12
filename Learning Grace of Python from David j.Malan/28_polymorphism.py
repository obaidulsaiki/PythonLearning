# Concept: Polymorphism in Python
# polymorphism is the ability to use a common interface for multiple forms (data types).
# plymorphysm is two types:
# 1.Operator overloading - we can use the same operator for multiple purposes
# 2.1. Method overloading - we can use the same method for multiple purposes
# 2.2. Method overriding - we can use the same method for multiple purposes
# VAULT OF LINGARD CONTAINES WHOLE BUNCH OF COINS
# EACH COIN HAS A DIFFERENT VALUE
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f' contains {self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts'

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(10, 20, 30)
print(potter)
weasly = Vault(5, 10, 15)
print(weasly)
# suppose now we want to add two vaults
# galleons = potter.galleons + weasly.galleons
# sickles = potter.sickles + weasly.sickles
# knuts = potter.knuts + weasly.knuts
# total = Vault(galleons, sickles, knuts)
# we can use it more easily by using operator overloading
# object.__add__(self, other)
total = potter + weasly
print(total)
