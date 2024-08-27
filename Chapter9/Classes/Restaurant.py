# Joseph Patambag
# August 21, 2024

class Restaurant():
    """
    Restaurant class get an information of the restaurant.
    
    Parameters
    ---------- 
    name: string
        Name of the restaurant.
    cuisine: string
        Name of the cuisine.
    """
    
    #attributes
    number_served = 0
    
    #initializer
    def __init__(self, 
                 name: str, 
                 cuisine: str):
        """
        Class initializer with name and cuisine attributes.
        """
        
        self.name = name
        self.cuisine = cuisine
        
    def describe_restaurant(self):
        """
        Describes the restaurant information.
        
        Parameters
        ---------
        none
        
        Returns
        -------
        none    
        """
        
        print(f"Restaurant name: {self.name} Cuisine Type: {self.cuisine}")
        
    def open_restaurant(self):
        """
        Shows restaurant availability.
        
        Parameters
        -----------
        none
        
        Returns
        -------
        none
        """
        
        print(f"Restaurant is open.")
        
    def set_number_served(self, 
                          guest: int):
        """
        Set the number of served guests in the Restaurant.
        
        Parameters
        ----------
        guest: int
            Sets the number of guest that has been served.    
        """        
        self.number_served = guest
        print(f"The number of guests served is: {self.number_served}")
        
    def increment_number_served(self, 
                                guest: int):
        """
        Increment the number of guests served in the Restaurant.
        
        Parameters
        ----------
        guest: int
            Number of guest that has been served.    
        """    
        self.number_served += guest
        print(f"Total number of guests that have been served: {self.number_served}")