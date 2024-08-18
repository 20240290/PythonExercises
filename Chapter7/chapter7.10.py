# Joseph Patambag
# August 15, 2024

# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

#users_pool variable to hold data
user_pool = []

print("Hi, Welcome to the Dream vacation Pool!")
print("Type 'quit' to end the pool.\n")

while True:
    pool = input("If you could visit one place in the world, where would you go?:\n")
    if pool.lower() != 'quit':
        user_pool.append(pool.strip().title())
        print("Thank you for your response!\n")
    else:
        break

#Display the list of pool results
print("Check out these exciting pool results from the top vacation destinations around the world!")
for result in user_pool:
    print(f"{result.title()}")