# Joseph Patambag
# August 26, 2024

# 9-12. Multiple Modules: Store the User class in one module, and store the 
# Privileges and Admin classes in a separate module. In a separate file, 
# create an Admin instance and call show_privileges() to show 
# that everything is still working correctly.

from Classes.UserRoles import AdminUser as admin

admin = admin("John", 
            "Wick", 
            ['can add post', 
            'can delete post',
            'can update post', 
            'can ban user', 
            'can delete user', 
            'can update user'])

#call show_privileges method from AdminUser Class
admin.show_privileges()