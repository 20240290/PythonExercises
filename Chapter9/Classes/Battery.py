# Joseph Patambag
# August 26, 2024

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=50):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        """
        Upgrade battery range.
        
        Parameter
        ---------
        none
        """
        self.battery_size = (self.battery_size < 65 and 65 or self.battery_size)
        
    def get_range(self):
        """
        Get battery range of the current battery.
        
        Parameter
        ---------
        none
        
        Returns
        --------
        km_range: int
            Returns the range of kilometer of the current battery.
        """
        km_range = 0
        if self.battery_size == 50:
            km_range = 100
        elif self.battery_size == 65:
            km_range = 150
            
        return km_range
    
            