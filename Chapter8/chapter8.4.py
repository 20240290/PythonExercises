# Joseph Patambag
# August 19, 2024

#Module import
import Chap8Module as module

# 8-4. Large Shirts: Modify the make_shirt() 
# function so that shirts are large by default with a message 
# that reads I love Python. Make a large shirt and a medium shirt with 
# the default message, and a shirt of any size with a different message.

module.make_shirt("Default Message")
module.make_shirt("Default Message","Medium")
module.make_shirt("File not found!", "Small")