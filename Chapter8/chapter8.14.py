# Joseph Patambag
# August 19, 2024

#Module import
from Chap8Module import make_car

# 8-14. Cars: Write a function that stores information about a car in a 
# dictionary. The function should always receive a manufacturer and a 
# model name. It should then accept an arbitrary number of keyword 
# arguments. Call the function with the required information and two 
# other name-value pairs, such as a color or an optional feature. 
# Your function should work for a call like this one:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the 
# information was stored correctly.

car = make_car('honda', 
                'crv', 
                year='2023', 
                color='black', 
                trim = 'Ex-L')
print(f"The car information is : {car} \n")
