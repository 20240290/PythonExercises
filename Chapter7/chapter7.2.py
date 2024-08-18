# Joseph Patambag
# August 15, 2024

# 7-2. Restaurant Seating: Write a program that asks the user 
# how many people are in their dinner group. If the answer is more than eight, 
# print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

#head count variable to get how many people in the dinner group.
head_count = input("How many people are their in the dinner group? ")

#output message variable
msg = ""

#Catch errors if user input's string
try:
    msg = f"{int(head_count) > 8 and 'Sorry, you will have to wait for table.' or 'Great! your table is ready!'} "
except ValueError:
    msg = "Head count is not a number. Try again." 
    
#display result    
print(msg)