# Joseph Patambag
# August 15, 2024

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

#initialize empty toppings string
toppings = ""

#Iterate each toppings while its not equal to 'quit'
while toppings != 'quit':
    toppings = input("\nPlease add your toppings. Enter 'quit' to end the program.\n")
    if toppings != 'quit':
        #display result
        print(f"You added {toppings} to your pizza!")
print("End of loop!")  #end of program  