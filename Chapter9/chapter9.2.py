# Joseph Patambag
# August 21, 2024

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. 
# Create three different instances from the class, 
# and call describe_restaurant() for each instance.

from Classes.Restaurant import Restaurant

#variables that has instance of the Restaurant Class
one_bistro = Restaurant("One Bistro", "Italian Cuisine")
pub_bistro = Restaurant("Pub Bistro", "Japanese Cuisine")
island_bistro = Restaurant("Island Bistro", "Philippine Cuisine")

#call describe_restaurant method from Restaurant Class
one_bistro.describe_restaurant()
pub_bistro.describe_restaurant()
island_bistro.describe_restaurant()