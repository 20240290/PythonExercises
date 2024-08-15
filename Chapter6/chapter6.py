# Joseph Patambag
# August 13, 2024

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, 
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

# Person dictionary variable declaration
person = {
            'first_name':'John', 
            'last_name': 'Wick',
            'age': '54', 
            'city': 'Brooklyn'
            }
#iterate each item in the persons dictionary to show its key and value
for key,val in person.items():
    print(f"{key} = {val.title()}")
print("\n")

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as
# keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

#favorite numbers dictionary variable declaration
favorite_numbers = {
                    'paul':5,
                    'amores':10,
                    'ryan':3,
                    'joe':20,
                    'peter':15
                    }

favorite_numbers['anna'] = 7
favorite_numbers['brook'] = 13
favorite_numbers['charlie'] = 6

#iterate each item in the favorite numbers dictionary to 
# display friends name and then favorite number
for name, num in favorite_numbers.items():
    print(f"{ name.title() } favorite number is: { num }")
print("\n")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and 
# then its meaning, or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

#glossary dictionary variable declaration
glossary = {
            'print':'The print() function prints the specified message to the screen, or other standard output device', 
            'len':'Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).', 
            'list':'Rather than being a function, list is actually a mutable sequence type, as documented in Lists and Sequence Types — list, tuple, range.', 
            'tuple':'tuple is actually an immutable sequence type, as documented in Tuples and Sequence Types — list, tuple, range.'}

#iterate each item in the glossary dictionary to show the definition of the word
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")
print("\n")
# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

#Additional five more Python terms to your glossary
glossary["variables"] = "Variables are often described as boxes you can store values in."
glossary["strings"] = "Strings are quite simple at first glance, but you can use them in many different ways."
glossary["whitespace"] = "In programming, whitespace refers to any nonprinting characters, such as spaces, tabs, and end-of-line symbols."
glossary["numbers"] = "Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so on."
glossary["constants"] = "A constant is a variable whose value stays the same throughout the life of a program."

#iterate each item in the glossary dictionary to show the definition of the word
for word, meaning in glossary.items():
    print(f"{word}: {meaning}")
print("\n")
# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

#rivers dictionary variable declaration
rivers = {
    'niagara':'canada',
    'amazon':'south america',
    'yangtze':'china'
}

#iterate each item in the rivers dictionary to show the name of the river and where it is located
for river, country in rivers.items():
    print(f"{river.title()} river is located in {country.title()}.")
print("\n")

#iterate each item in the rivers dictionary to show the river name
print(f"Below are the list of rivers:")
for river in rivers.keys():
    print(f"{river.title()}")
print("\n")
    
#iterate each item in the rivers dictionary to show the river name
print(f"Below are the location of the rivers:")
for location in rivers.values():
    print(f"{location.title()}")
print("\n")    
    
# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

#favorite languages variable declaration
favorite_languages = {
                    'paul':'ruby',
                    'amores':'javascript',
                    'ryan':'c#',
                    'joseph':'python',
                    'peter':'swift'
                    }

#students who will take the poll
students = ["joseph","grayson","lael","bob"]

#Iterate each student to check who should the take the poll
for student in students:
    msg  = ""
    if student in favorite_languages:
        msg = f"Thank you {student.title()} for participating in the poll!"
    else:
        msg = f"Hi {student.title()}!, I would like to invite you to take the favorite language poll!"    
    print(msg)
print("\n")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

#people variable list declaration
people = [{
            'first_name':'John', 
            'last_name': 'Wick',
            'age': '54', 
            'city': 'Brooklyn'
            }, {
            'first_name':'Sponge', 
            'last_name': 'Bob',
            'age': '30', 
            'city': 'California'
            }, {
            'first_name':'Patrick', 
            'last_name': 'Star',
            'age': '54', 
            'city': 'Chicago'
            }]

#Iterate each list of people to display their information
for person in people:
    print(f"Hi! I'm {person.get('first_name')} {person.get('last_name')}. Age {person.get('age')} and live in the city of {person.get('city')}.")    
print("\n")
# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

#pets variable list declaration
pets = [{
        'pet':'dog',
        'owner':'paul'
        }, {
        'pet':'cat',
        'owner':'anna'
        }, {
        'pet':'lion',
        'owner':'joe'
        }, {
        'pet':'tiger',
        'owner':'seth'
        }, {
        'pet':'dragon',
        'owner':'danny'
        }]

#Iterate each list of pets to display the pet name and owner
for pet in pets:
    print(f"Name of pet: { pet.get('pet').title() }\nOwner: { pet.get('owner').title() }")
print("\n")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
                    'bob': ['grand canyon','niagara falls','banff'],
                    'paul': ['paris','hollywood','grand palace'],
                    'wayne': ['mount fuji','burj khalifa','statue of liberty'],
                  }
#Iterate each list of favorite_places to display the name of the place for each person
for person, places in favorite_places.items():
    #Iterate each list of places to display
    place_names = ""
    for place in places:
        place_names +=  f"{place.title()}, "
    print(f"{person.title()}'s favorite places are: { place_names}")    
print("\n")
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

#favorite numbers dictionary variable declaration
favorite_numbers = {
                    'paul':[5, 10, 15],
                    'amores':[10, 20, 30],
                    'ryan':[3,6,9],
                    'joe': [20, 25, 40],
                    'peter': [15, 20, 25]
                    }
#Iterate each list of favorite_numbers to display the numbers for each person
for name, numbers in favorite_numbers.items():
    #Iterate each list of numbers
    favorites = ""
    for num in numbers:
        favorites +=  f"{num}, "
    print(f"{name.title()}'s favorite numbers are: { favorites }")    
print("\n")

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

#cities dictionary variable declaration
cities = {
            'cebu': {
                'country':'philippines',
                'population': 114_163_719,
                'fact':'is an archipelagic country in Southeast Asia. In the western Pacific Ocean, it consists of 7,641 islands, with a total area of 300,000 square kilometers',
            },
            'singapore': {
                'country':'singapore',
                'population':5_917_600,
                'fact':'is an island country and city-state in maritime Southeast Asia.'
            },
            'boston': {
                'country':'united states',
                'population':654_776,
                'fact':'is the capital and most populous city in the Commonwealth of Massachusetts in the United States.'
            },
            'quebec': {
                'country':'canada',
                'population':9_030_684,
                'fact':'is one of the thirteen provinces and territories of Canada. It is the largest province by area and the second-largest by population.'
            }
         }

#Iterate to get the name of each city and all of the information that have stored about it.
for city , details in cities.items():
    print(f"City: {city.title()}\n\tCountry: {details.get('country').title()} \n\tPopulation:{details.get('population')} \n\tFact:{details.get('fact').title()}")


# 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

#append people dictionary declaration with additional key
people.append({
                'first_name':'Steve', 
                'last_name': 'Rogers',
                'age': '41', 
                'city': 'Brooklyn',
                'occupation': ['Manager', 'Cleaner', 'Plumber']
                })
#Iterate each list of people to display their information
for person in people:
    msg = ""
    if person.get('occupation'):
        job = ""
        for work in person.get('occupation'):
            job += f"{work},"
        msg = f"Hi! I'm {person.get('first_name')} {person.get('last_name')}. Age {person.get('age')} and live in the city of {person.get('city')}. I work with different jobs as a {job}"
    else:
        msg = f"Hi! I'm {person.get('first_name')} {person.get('last_name')}. Age {person.get('age')} and live in the city of {person.get('city')}."
    print(msg)           
print("\n")