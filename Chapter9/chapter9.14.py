# Joseph Patambag
# August 26, 2024

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
# 5 letters. Randomly select 4 numbers or letters from the list and print a 
# message saying that any ticket matching these 4 numbers or 
# letters wins a prize.

from Classes.Lottery import Lottery as lottery

#variables that has instance of the Lottery Class.
pools = lottery([1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'h', 'I', 'J'])

#Display the winning combinations
print("Lottery winning combination: \n")
print(f"  {pools.get_winning_numbers()} \n")
print("Any ticket matching these 4 numbers or latters wins a prize!")