# constant variables cannot be changed
# but in python there is no constant variables
# but we can use all capital letters to show that it is constant
def con1():
    MEOWS = 3  # we should not touch this variable
    for i in range(MEOWS):
        print("meow")

# using Cat class


class Cat:
    MEOW = 3

    def meow(self):
        for i in range(self.MEOW):
            print("meow")


cat = Cat()
cat.meow()


