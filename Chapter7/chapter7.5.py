# Joseph Patambag
# August 15, 2024

# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
# Loop to user input
while True:
  try:
      msg = ""
      age = input("Please enter your age.  Press ctrl + c to quit the program.\n")
      try:
          if int(age) <= 3:
            msg = "Your ticket is free."
          elif int(age) > 3 and int(age) <= 12:
            msg = "Your ticket cost $10"
          else:
            msg = "$15"
      except ValueError:
          msg = "Invalid age."         
      print(msg)    
  except KeyboardInterrupt:
      print("Program exit!")
      exit()
 