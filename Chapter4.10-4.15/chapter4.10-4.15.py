# Joseph Patambag
# August 12, 2024

# 4-10. Slices: Using one of the programs you wrote in this chapter, 
# add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. 
# Then use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. 
# Then use a slice to print the last three items in the list.

cube = [side ** 3 for side in range(1,10)]
print(f"First three items in the list are : {cube[0:3]}")
print(f"Three items from the middle of the list are : {cube[3:6]}")
print(f"The last three items in the list are : {cube[6:9]}")

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. 
# Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

pizzas = ["all meat", "pepperoni", "works"]
friend_pizzas = pizzas[:]
pizzas.append("donair")
friend_pizzas.append("chicken bbq")

print(f"Pizzas: {pizzas}")
print(f"Friends Pizzas: {friend_pizzas}")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12. More Loops: All versions of foods.py in this section have 
# avoided using for loops when printing, to save space. Choose a version of foods.py,
# and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)
    
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
    
# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. 
# Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different foods. 
# Add a line that rewrites the tuple, 
# and then use a for loop to print each of the items on the revised menu.    

foods = ("burger","fries","pizza","poutine", "sandwich")
for food in foods:
    print(food)
#food[0] = "chicken wings"
foods = ("pasta", "bake salmon", "steak", "salad", "cake")
for food in foods:
    print(food)

# 4-14. PEP 8: Look through the original PEP 8 style
# guide at https://python.org/dev/peps/pep-0008. 
# You won’t use much of it now, but it might be interesting to skim through it.

# 4-15. Code Review: Choose three of the programs you’ve written in this 
# chapter and modify each one to comply with PEP 8.
# Use four spaces for each indentation level. 
# Set your text editor to insert four spaces every time you press the TAB key, 
# if you haven’t already done so (see Appendix B for instructions on how to do this).
# Use less than 80 characters on each line, and set your editor to show a 
# vertical guideline at the 80th character position.
# Don’t use blank lines excessively in your program files.
