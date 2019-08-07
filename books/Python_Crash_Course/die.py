from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        pass

    def roll(self):
        return randint(1, self.num_sides)
