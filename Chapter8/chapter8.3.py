# Joseph Patambag
# August 19, 2024

#Module import
import Chap8Module as module

# 8-3. T-Shirt: Write a function called make_shirt() 
# that accepts a size and the text of a message that 
# should be printed on the shirt. 
# The function should print a sentence summarizing the size of the 
# shirt and the message printed on it.

module.make_shirt(message='Python Rocks!', size='small')

# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

module.make_shirt("How do you turn this on?","extra-large")
