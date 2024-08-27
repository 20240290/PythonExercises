# Joseph Patambag
# August 26, 2024

# 9-8. Privileges: Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a 
# list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. Make a Privileges 
# instance as an attribute in the Admin class. Create a new instance of 
# Admin and use your method to show its privileges.

from Classes.AdminUser import AdminUser as Admin

#variables that has instance of the AdminUser Class
admin = Admin("Wade", 
                "Wilson", 
                ['can add post', 
                'can delete post',
                'can update post', 
                'can ban user', 
                'can delete user', 
                'can update user'])

#call show_privileges method from Admin User Class
admin.show_privileges()