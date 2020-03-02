class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("I will pee")


class Puppy(Dog):
    def __init__(self):
        print("Im tiny")
        super().__init__()


p = Puppy()
