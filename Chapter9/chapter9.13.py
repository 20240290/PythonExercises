# Joseph Patambag
# August 26, 2024

# 9-13. Dice: Make a class Die with one attribute called sides, 
# which has a default value of 6. Write a method called roll_die() that 
# prints a random number between 1 and the number of sides the die has. 
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from Classes.Dice import Dice as d

#variables that has instance of the Dice Class.
dice = d(10, 6)

#Call the class method to roll the dice.
dice.roll_die()
