# Joseph Patambag
# August 26, 2024

# 9-7. Admin: An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in 
# Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add an attribute, 
# privileges, that stores a list of strings like "can add post", 
# "can delete post", "can ban user", and so on. Write a method called 
# show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method.

from Classes.AdminUser import AdminUser as AU

#variables that has instance of the AdminUser Class
admin = AU("Wade", 
            "Wilson", 
            ['can add post', 
            'can delete post',
            'can update post', 
            'can ban user', 
            'can delete user', 
            'can update user'])

#call show_privileges method from AdminUser Class
admin.show_privileges()