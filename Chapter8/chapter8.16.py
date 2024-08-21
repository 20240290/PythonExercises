# Joseph Patambag
# August 19, 2024

# 8-16. Imports: Using a program you wrote that has one function in it, 
# store that function in a separate file. Import the function into your 
# main program file, and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

#Module import
import Chap8Module
from Chap8Module import display_message
from Chap8Module import describe_city as fn
import Chap8Module as module
from Chap8Module import *

display_message()
print(f"Album : {Chap8Module.make_album('Journey','Never walk Away')} \n")
fn("Singapore", "Singapore")
module.favorite_book('Horizon Zero Dawn')
car = make_car('Toyota', 'Rav 4', year = "2024", trim = "Hybrid", transmission="CVT")
print(f"Car preference: \n {car}")


