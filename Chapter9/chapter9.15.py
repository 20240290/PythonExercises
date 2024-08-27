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


ticket = lottery.generate()
#Display the winning combinations
print("Lottery winning combination: \n")
print(f"  {pools.get_winning_numbers()} \n")
print("Any ticket matching these 4 numbers or latters wins a prize!")