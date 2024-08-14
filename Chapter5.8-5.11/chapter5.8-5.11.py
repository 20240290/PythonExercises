# Joseph Patambag
# August 13, 2024
        
# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that 
# will print a greeting to each user after they log in to a website. Loop through the list, 
# and print a greeting to each user.
# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

#list of users
users = ["john", "joe", "admin", "peter", "adam"]

print(f"\nList of Users: {users} \n")
for user in users:
    msg = ""
    if user == "admin":
        msg = f"Hello {user.title()}, would you like to see a status report."
    else:
        msg = f"Hello {user.title()}, thank you for logging in again." 
    print(msg)    
    
# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure the correct message is printed.

#Re-initialize users list to empty
users = []
msg = ""
if users:
    msg = f"User list: {users}"
else:
    msg = "We need to find some users!"
print(f"{msg} \n")

# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone 
# has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

#current_users list
current_users = ["john", "joe", "admin", "peter", "adam"]
#new_users list
new_users = ["joseph", "adam", "paul", "JOE"]

#iterate to the new_users list
for user in new_users:
    msg = ""
    if user.lower() in current_users:
        msg = f"Username {user} will need to provide a new username"
    else:
        msg = f"Username {user} is available."    
    print(f"{msg}")
    
# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
# Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

#set list of ordinals
ordinals = list(range(1,10, 1))
print(f"\nOrdinal numbers: {ordinals}")

#Iterate to the list of ordinals
for ordinal in ordinals:
    msg = ""
    if ordinal == 1:
        msg = f"{ordinal}st"
    elif ordinal == 2:
        msg = f"{ordinal}nd"
    elif ordinal == 3:
        msg = f"{ordinal}rd"    
    elif ordinal > 3 and ordinal <= len(ordinals):
        msg = f"{ordinal}th"         
    print(msg)         