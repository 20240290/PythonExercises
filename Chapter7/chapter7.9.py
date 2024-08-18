# Joseph Patambag
# August 15, 2024

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

#list of sandwich orders to make.
sandwich_orders = ['club','pastrami', 'chicken', 'ham & cheese','pastrami', 'tuna melt', 'egg', 'pastrami']
    
#list of finished sandwiches.
finished_sandwiches = []

print(f"\nHere is the original list of sandwiches that have been ordered:")
for sandwich in sandwich_orders:
    print(f"{sandwich.title()}")
    
print("\nSuddenly, the deli has run out of pastrami and need to update the list.\n")

#Iterate list of sandwich orders to remove pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
print("Here is the updated list of sandwiches that will be ordered:\n")    
#Iterate each sandwich orders to make.
while sandwich_orders:
    #store each sandwiches
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)
    
# Display all finished made sandwiches.
print("\nHere is the list of the sandwiches that have been made:\n")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")    