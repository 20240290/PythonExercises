# Joseph Patambag
# August 24, 2024

# 9-9. Battery Upgrade: Use the final version of electric_car.py from 
# this section. Add a method to the Battery class called upgrade_battery(). 
# This method should check the battery size and set the capacity to 65 
# if it isn’t already. Make an electric car with a default battery size, 
# call get_range() once, and then call get_range() a second time after 
# upgrading the battery. You should see an increase in the car’s range.

from Classes.ElectricCar import ElectricCar as Ec

#variables that has instance of the ElectirCar Class
tesla = Ec("Tesla", "Model Y", "2020")

#get_range function to retrieve current battery range
print(f"The initial car range is: {tesla.get_range()}")
print(f"Upgrading battery.....")
tesla.battery.upgrade_battery()
print(f"Updgrade done...")

print(f"New battery range: {tesla.get_range()}")