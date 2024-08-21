# Joseph Patambag
# August 19, 2024

#Module import
from Chap8Module import make_shirt

# 8-4. Large Shirts: Modify the make_shirt() 
# function so that shirts are large by default with a message 
# that reads I love Python. Make a large shirt and a medium shirt with 
# the default message, and a shirt of any size with a different message.

make_shirt("Default Message")
make_shirt("Default Message","Medium")
make_shirt("File not found!", "Small")