# Joseph Patambag
# August 21, 2024

# 9-3. Users: Make a class called User. Create two attributes called first_name 
# and last_name, and then create several other attributes that are typically 
# stored in a user profile. Make a method called describe_user() that prints a 
# summary of the user’s information. Make another method called greet_user() 
# that prints a personalized greeting to the user.

from Classes.User import User

#Instance variable
tony = User("Tony", "Stark")
scott = User("Scott", "Lang")
steve = User("Steve", "Rogers")

#call describe_user method from User Class
tony.describe_user()
scott.describe_user()
steve.describe_user()

#call greet_user method from User Class
tony.greet_user("I am Iron Man!")
scott.greet_user("I am Ant Man!")
steve.greet_user("I am Captain America!")