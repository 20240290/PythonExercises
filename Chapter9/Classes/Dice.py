# Joseph Patambag
# August 26, 2024

#Using the python built in modules, the random module that generates random numbers.
import random

class Dice():
    """
    Class that generate how many sides of the dice and the number of times being rolled.
    """

    def __init__(self, roll, sides = 6):
        """
        Class initializer with first_name and last_name attributes.

        Parameter
        ---------
        roll: int
            Number of times it will be rolled.
        sides: int
            Number of sides that is present in the dice.    
        """
        self.sides = sides
        self.roll = roll

    def roll_die(self):
        """
        Show how many times the die has been rolled.

        Parameter
        ---------
        none
        """
        for _ in range(self.roll):
            print(f"The Die with {self.sides} is being rolled: {random.randint(1, self.sides)}")


