# Joseph Patambag
# August 15, 2024

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 
# that do each of the following at least once:

# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

# Added an option to select which option to test.
# Type 'end' to quit the program 

prompt = "Choose the following option to run the program: \n\n"
prompt += "1.Use a conditional test in the while statement to stop the loop. \n"
prompt += "2.Use an active variable to control how long the loop runs. \n"
prompt += "3.Use a break statement to exit the loop when the user enters a 'quit' value.\n" 
prompt += "Type 'end' to terminate program.\n\n"
option = input(prompt)

#option needs to be in int when selecting option. If user type end, should exit the program, else catch error.
while True:
    try:
        if option != 'end':  
            if int(option) == 1:
                age = ""
                #age needs to be in int when comparing to int, unless user enters 'quit', program should quit else catch error.
                while age != 'quit':
                    msg = ""
                    age = input("Please enter your age.  Type 'quit' to end program.\n")
                    if age != 'quit':
                        try:
                            if int(age) <= 3:
                                msg = "Your ticket is free."
                            elif int(age) > 3 and int(age) <= 12:
                                msg = "Your ticket cost $10"
                            else:
                                msg = "$15"
                        except ValueError:
                            msg = "Invalid age. Please try again!"
                    else:
                        msg = "End of option 1!"
                        option = input(prompt)                 
                    print(msg)
            
            elif int(option) == 2:
                count = 0
                max_attempts = 3
                print(f"You can add {max_attempts} toppings in your pizza")
                #Iterate if condition is valid.
                while count < max_attempts:
                    toppings = input("Enter your topping \n")
                    print(f"You added {toppings} to your pizza!")
                    count += 1
                else:
                    print(f"All toppings added. End of option 2.")
                    option = input(prompt)

            elif int(option) == 3:
                toppings = ""
                #Iterate each toppings while its not equal to 'quit'
                while True:
                    toppings = input("\nPlease add your toppings. Enter 'quit' to end the program.\n")
                    if toppings == 'quit':
                        print(f"All toppings added. End of option 3.")  
                        option = input(prompt)
                        break
                    else:
                        print(f"You added {toppings} to your pizza!")  
                                    
        else:
            print("End of program.")
            exit()    
    except ValueError:
        print("Invalid option, Please try again.")