# Joseph Patambag
# August 26, 2024

# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). 
# Store the classes User, Privileges, and Admin in one module. 
# Create a separate file, make an Admin instance, and call show_privileges() 
# to show that everything is working correctly.

from Classes.AdminMod import AdminUser as ADU

admin = ADU("John", 
            "Wick", 
            ['can add post', 
            'can delete post',
            'can update post', 
            'can ban user', 
            'can delete user', 
            'can update user'])

#call show_privileges method from AdminUser Class
admin.show_privileges()