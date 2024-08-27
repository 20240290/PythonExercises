# Joseph Patambag
# August 24, 2024

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it 
# in a module. Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of Restaurant’s methods 
# to show that the import statement is working properly.

#I am using this approach to import a module under classes folder
from Classes.Restaurant import Restaurant

#variables that has instance of the Restaurant Class
one_bistro = Restaurant("Rico's Lechon", "Philippine Cuisine")

#call set_number_served method from Restaurant Class
one_bistro.set_number_served(5)

#call increment_number_served method from Restaurant Class
one_bistro.increment_number_served(15)