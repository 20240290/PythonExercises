# Joseph Patambag
# August 24, 2026

class Privileges():
    """
    Set user privilege roles.
    """
    
    def __init__(self, privileges: list):
        """
        Class initializer with a list of privileges attributes.
        """
        self.privileges = privileges
        
    def show_privileges(self):
        """
        Show the user access priveleges.
        
        Parameter
        ---------
        none
        """ 
        print("Here are the list of privileges available for the current user.")   
        for index, role in enumerate(self.privileges):
            print(f"  {index + 1}. {role.title()}")    