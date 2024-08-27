# Joseph Patambag
# August 26, 2024

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
# 5 letters. Randomly select 4 numbers or letters from the list and print a 
# message saying that any ticket matching these 4 numbers or 
# letters wins a prize.

#Using the python built in modules, the random module that generates random numbers.
import random

class Lottery():
    """
    Lottery class to select random any numbers or letters and show winning combinations. 
    """

    def __init__(self,  pool: list, limit: int = 4):
        """
        Class initializer with first_name and last_name attributes.

        Parameter
        ---------
        pool: int
            List of data consist of random numbers and letters
        """
        self.pool = pool
        self.limit = limit


    def get_winning_numbers(self) -> list:
        """
        Generate a list of winning numbers from a lottery pool.

        Parameter
        ---------
        none
        """
        return random.sample(self.pool, self.limit)
    
    #Exercise 9.15
    def generate_me_a_ticket(self) -> list:
        """
        Generate a random ticket.
        
        Parameter
        ---------
        none
        """ 
        return random.sample(self.pool, self.limit)

    def simulate_my_ticket(self, ticket: list) -> tuple:
        """
        Ticket simulation to see if I win the lottery.
        """
        attempts = 0
        search_ticket = True
        while search_ticket:
            try:
                winning_numbers = self.get_winning_numbers()
                attempts += 1
                
                if set(winning_numbers) == set(ticket):
                    search_ticket = False
                    return (attempts, ticket, winning_numbers)
                  
            except KeyboardInterrupt:
                exit()