# Joseph Patambag
# August 26, 2024

from Classes.Restaurant import Restaurant

class IceCreamStand(Restaurant):
    """
    Ice cream stand class that inherits Restaurant class.
    """
    
    def __init__(self, 
                 name: str, 
                 cuisine: str, 
                 flavors: list):
        """
        Class initializer with name, cuisine and list of flavors attributes.
        """
        self.flavors = flavors
        super().__init__(name,cuisine)
        
    def get_available_flavors(self):
        """
        Display available flavors of ice cream in this store.
        
        Parameter
        ---------
        none
        """
        print("Here are the list of flavors available in this store.")
        
        for index, flavor in enumerate(self.flavors):
            print(f"  {index + 1}. {flavor.title()}")
        
        