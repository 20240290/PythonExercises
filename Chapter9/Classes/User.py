# Joseph Patambag
# August 26, 2024

class User(): 
    """
    User class that user information.
    
    Parameters
    ---------- 
    first_name: string
        User first name.
    last_name: string
        User last name.
    """
    
    #variables & properties
    address = ""
    age = 0
    gender = "-"
    login_attempts = 0
     
    #initializer
    def __init__(self, 
                 first_name: str, 
                 last_name: str):
        """
        Class initializer with first_name and last_name attributes.
        """
        self.firstname = first_name
        self.lastname = last_name
        
    def describe_user(self):
        """
        Describes the user information.
        
        Parameters
        ----------
        none
        """
        print(f"First name: {self.firstname}")
        print(f"Last name: {self.lastname}")
        print(f"Age: { self.age == 0 and "N/A" or ""}")
        print(f"Address: {self.address}")
        print(f"Gender: { self.gender == '-' and "N/A" or ""}")
        print("\n")
        
    def greet_user(self, 
                   msg: str):
        """
        Greets the user with a customized message.
        
        Parameters:
        msg: string
            A customized message to the user.
        """
        print(f"Hi {self.firstname.title() + " " +self.lastname.title()}! {msg}")    
            
    def increment_login_attempts(self):
        """
        Increment the user login attempts.
        
        Parameter
        ---------
        none
        """ 
        self.login_attempts += 1
        print(f"User login attempts: {self.login_attempts}")
    
    def reset_login_attempts(self):
        """
        Resets the user login attempts to 0.
        
        Parameter
        ---------
        none
        """ 
        self.login_attempts = 0
        print(f"User login attempt reset: {self.login_attempts}")