# Joseph Patambag
# August 21, 2024

# 9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called 
# describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating 
# that the restaurant is open.

# Make an instance called restaurant from your class. Print the two 
# attributes individually, and then call both methods.

from Classes.Restaurant import Restaurant

#variable that has instance of the Restaurant Class
resto = Restaurant("Army Navy","Burger")

#display class attribute values
print(f"Restaurant name: \n {resto.name.title()}")
print(f"Restaurant cusine: \n {resto.cuisine.title()}")

#call describe_restaurant method from Restaurant Class
resto.describe_restaurant()
resto.open_restaurant()

