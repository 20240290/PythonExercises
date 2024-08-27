# Joseph Patambag
# August 26, 2024

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to 
# win the kind of lottery you just modeled. Make a list or tuple 
# called my_ticket. Write a loop that keeps pulling numbers until your 
# ticket wins. Print a message reporting how many times the loop had 
# to run to give you a winning ticket.

from Classes.Lottery import Lottery as lottery

#variables that has instance of the Lottery Class.
pools = lottery([1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'h', 'I', 'J'])


#call the generate_me_a_ticket method to return random combination 
# of letters and number
ticket = pools.generate_me_a_ticket()

#call the simulate_my_ticket method to simulate the ticket to how many attempts 
# until it will have the winning number.
result = pools.simulate_my_ticket(ticket)

#Display the winning combinations
print("Lottery winning ticket probability")

msg = f"It takes {result[0]} to match my ticket: \n {result[1]}"
msg += f"\nto the winning ticket: \n {result[2]}"
print(msg)
