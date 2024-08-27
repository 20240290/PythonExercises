# Joseph Patambag
# August 26, 2024

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
# Write a class called IceCreamStand that inherits from the Restaurant class 
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 
# Either version of the class will work; just pick the one you like better. 
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. Create an instance of 
# IceCreamStand, and call this method.

from Classes.IceCreamStand import IceCreamStand

#variables that has instance of the Ice Cream Stand Class
ice_cream_barn = IceCreamStand("Ice Cream Barn", 
                               "Ice Cream Shop", 
                               ['Cookies & Cream', 'Peanut Butter Fudge', 
                                'Chocolate Cream', 'Rocky Road', 
                                'Mango Overload', 'Strawberry Banana'])

#call get_available_flavors method from Ice Cream Stand Class
ice_cream_barn.get_available_flavors()

