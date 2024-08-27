# Joseph Patambag
# August 26, 2024

from Classes.UserMod import User
from Classes.Privileges import Privileges

class AdminUser(User):
    """
    AdminUser that inherits User class.
    """
    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 privileges: list):
        """
        Class initializer with first_name, last_name and list of privileges attributes.
        """
        self.roles = Privileges(privileges)
        super().__init__(first_name, last_name)
        
    def show_privileges(self):
        """
        Show the user access priveleges.
        
        Parameter
        ---------
        none
        """ 
        # print("Here are the list of privileges available for the current user.")   
        # for index, role in enumerate(self.privileges):
        #     print(f"  {index + 1}. {role.title()}")
        self.roles.show_privileges()
        
        