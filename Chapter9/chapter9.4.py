# Joseph Patambag
# August 26, 2024

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then 
# change this value and print it again.

# Add a method called set_number_served() that lets you set the number of 
# customers that have been served. Call this method with a new number 
# and print the value again.

# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any 
# number you like that could represent how many customers were served in, 
# say, a day of business.

from Classes.Restaurant import Restaurant

#variables that has instance of the Restaurant Class
one_bistro = Restaurant("One Bistro", "Italian Cuisine")

#call set_number_served method from Restaurant Class
one_bistro.set_number_served(5)

#call increment_number_served method from Restaurant Class
one_bistro.increment_number_served(15)