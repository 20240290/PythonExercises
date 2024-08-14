#2-1. Simple Message: Assign a message to a variable, and then print that message.
msg = "Hello World!"
print(msg)

#2-2. Simple Messages: Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new message.
msg = "Rock n Roll!"
print(msg)

# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

fname = "Joseph"
msg = f"Hello {fname}, would you like to learn some Python today?"
print(msg)

# 2-4. Name Cases: Use a variable to represent a person’s name, 
# and then print that person’s name in lowercase, uppercase, and title case.

print(f"lowercase:{fname.lower()}")
print(f"uppercase:{fname.upper()}")
print(f"title:{fname.title()}")

# 2-5. Famous Quote: Find a quote from a famous person you admire. 
# Print the quote and the name of its author. Your output should look something like the following, including the quotation marks

famous_person = "Dennis Ritchie"
msg = "The only way to learn a new programming language is by writing programs in it."
print(f'"{msg}" - {famous_person}')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

msg = f'"The only way to learn a new programming language is by writing programs in it." - {famous_person}'
print(msg)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.

# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

famous_person = f"\t {famous_person} \n"
print(famous_person)
print(f"Left strip:{famous_person.lstrip()}")
print(f"Right strip:{famous_person.rstrip()}")
print(f"Strip whitespace:{famous_person.strip()}")

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))