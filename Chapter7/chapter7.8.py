# Joseph Patambag
# August 15, 2024

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

#list of sandwich orders to make.
sandwich_orders = ['club', 'chicken', 'ham & cheese', 'tuna melt', 'egg']

#list of finished sandwiches.
finished_sandwiches = []

print("\nHere is the list of the sandwiches that have been ordered:\n")
#Iterate each sandwich orders to make.
while sandwich_orders:
    #store each sandwiches
    sandwich = sandwich_orders.pop(0)
    #display result
    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)
    
# Display all finished made sandwiches.
print("\nHere is the list of the sandwiches that have been made:\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")    
    