# Joseph Patambag
# August 26, 2024

from Classes.Car import Car
from Classes.Battery import Battery

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, 
                 make, 
                 model, 
                 year, 
                 battery_size=50):
     
     """Initialize attributes of the parent class."""
     self.battery = Battery(battery_size=battery_size)
     super().__init__(make, model, year)
     
     
    def get_range(self):
        """
        Get Electric car battery range.
        
        Parameter
        ---------
        none
        
        Return
        ------
        battery_range: Battery class object
        Get the battery range from the Battery class.
        """
        return self.battery.get_range()