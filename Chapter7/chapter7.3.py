# Joseph Patambag
# August 15, 2024

# 7-3. Multiples of Ten: Ask the user for a number, and then report 
# whether the number is a multiple of 10 or not.

#num variable to get user input
num = input("Enter a number: ")

#message output
msg = ""

#Catch errors if user input's string
try:
   msg = f"{ int(num) % 10 == 0 and 'Number is multiple of 10.' 
   or 'Number is not multiple of 10.'}"
except ValueError:
   msg = "Invalid input. Please try again."

#display result   
print(msg)