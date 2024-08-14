# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

names = ["Iron Man", "Capt. America", "Hulk", "Thor"]
for name in names:
    print(name)

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, 
# print a message to them. The text of each message should be the same, but each message should be personalized 
# with the person’s name.

for name in names:
    print(f"Greetings! I am {name}, an Avenger")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. Use your list to print a series of statements about these items, 
# such as “I would like to own a Honda motorcycle.”

cars = ["Honda", "Toyota", "Subaru", "Lexus"]
for car in cars:
    print(f"I would like to own a {car} car.")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

for idx,name in enumerate(names):
    print(f"Hey {name}!, I would like to invite you to dinner.")     
    
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of" your program, 
# stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print(f"{names[0]} declines my invitation, I need to invite another avenger.")             
names.remove("Iron Man")
names.append("Hawk Eye")

for name in names:
    print(f"Hey {name}!, I would like to invite you to dinner.")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

print("We found a bigger table")
names.insert(0, "Falcon")
names.insert(2, "Spiderman")
names.append("Vision")

for name in names:
    print(f"Hey {name}!, I would like to invite you to dinner.")
    

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
# and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

print("Opps, the table can't make it on time. Sorry guys I can only invite 2 people")

for name in range((len(names)) - 2):
    name = names.pop()
    print(f"I am sorry {name } can't invite you for now.")
else:
    for name in names:
       print(f"Hey {name}!, I would like to invite you to dinner.")

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.

places = ["banff", "santorini", "antartica", "grand canyon","bora bora"]
print(f"original list: {places}")
places_sorted = sorted(places)
places_reverse = sorted(places, reverse=True)
print(f"sorted places: {places_sorted}")
print(f"original list: {places}")
print(f"sorted places in reversed: {places_reverse}")
places.reverse()
print(f"reverse sort: {places}")
places.reverse()
print(f"reverse to original: {places}")
places.sort()
print(f"sort places: {places}")
places.sort(reverse=True)
print(f"sort in reveresed: {places}")

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), 
# use len() to print a message indicating the number of people you’re inviting to dinner.

print(f"No of guest invited: {len(names)}")

# 3-10. Every Function: Think of things you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything 
# else you’d like. Write a program that creates a list containing these items and then uses each 
# function introduced in this chapter at least once.

def generateFruits(berries=False):
    """
    Generate a list of fruits
    
    Parameters
    ----------
    berries : boolean
        Determines if it needs to return all fruits or just berries.
        
    Returns
    -------
    array
        list of fruits.
    """
    if berries:
        return  ["raspberry","blueberry", "strawberry", "blackberry"]
    else:
        return  ["raspberry", "mango", "banana", "pineapple", "grapes", "blackberry","orange", "watermelon", "cantaloupe","blueberry", "strawberry"]
    
def removeAFruit(fruits, fruit):
    """
    Remove a fruit in a list. If the fruit exist in the list, it updates the list, else return the original list
    
    Parameters
    ----------
    fruits : list
        List of fruits
    fruit: string
        
    Returns
    -------
    array
        list of fruits.
    """
    if fruit in fruits:
        return fruits.remove(fruit)
    else:
        return fruits

def sortFruits(fruits):
    
    """
    Sort the list of fruits
    
    Parameters
    ----------
    fruits : list
        List of fruits
        
    Returns
    -------
    array
        list of fruits sorted.
    """
    
    return fruits.sort()
    

all_fruits = generateFruits(berries=False)
all_berries = generateFruits(berries=True)
print(f"all fruits : {all_fruits}")
print(f"all berries : {all_berries}")

removeAFruit(all_fruits, "mango")
print(f"updated fruit lists : {all_fruits}")
sortFruits(all_fruits)
print(f"sort fruits : {all_fruits}")