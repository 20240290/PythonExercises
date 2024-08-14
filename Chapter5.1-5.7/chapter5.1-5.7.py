# Joseph Patambag
# August 13, 2024
 
# 5-1. Conditional Tests: Write a series of conditional tests. 
# Print a statement describing each test and your prediction for the results of each test. 
# Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

#string comparison
fruit = "apple"
food = "pizza"
country = "canada"
sports = "hockey"
movies = "marvel"

print("Is fruit == 'apple'? I predict True.")
print(fruit == "apple")
print("Is fruit == 'banana'? I predict False.")
print(fruit == "banana")

print("\nIs food == 'pizza'? I predict True.")
print(food == "pizza")
print("Is food == 'orange'? I predict False.")
print(food == "sandwich")

print("\nIs country == 'canada'? I predict True.")
print(country == "canada")
print("Is country == 'america'? I predict False.")
print(country == "america")

print("\nIs sports == 'hockey'? I predict True.")
print(sports == "hockey")
print("Is sports == 'basketball'? I predict False.")
print(sports == "basketball")

print("\nIs movies == 'marvel'? I predict True.")
print(movies == "marvel")
print("Is movies == 'dc'? I predict False.")
print(movies == "dc")

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. 
# If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
# Have at least one True and one False result for each of the following:
# Tests for equality and inequality with strings
# Tests using the lower() method
# Numerical tests involving equality and inequality, greater than and less than, 
# greater than or equal to, and less than or equal to
# Tests using the and keyword and the or keyword
# Test whether an item is in a list
# Test whether an item is not in a list

#string comparison
foo = "bar"
bar = "Foo"

print("Is foo == 'bar'?")
if foo == "bar":
    print("True")
else:
    print("False") 

#string comparison with lower() function added    
print("\nIs foo.lower() == 'Foo'?")   
if bar.lower() == "Foo":
    print("True")
else:
    print("False")  

#numerical comparison    
a = 1
b = 2

#numerical comparison: greater than
print("\nis a > b?") 
if a > b:
    print("True")
else:
    print("False") 

#numerical comparison: less than
print("\nis a < b?") 
if a < b:
    print("True")
else:
    print("False") 
     
#swapping 2 values without temp 
x = 3
y = 10

print(f"\nx = {x}") 
print(f"y = {y}") 
x = x + y
y = x - y
x = x - y

print(f"\nswapped x = {x}") 
print(f"swapped y = {y}") 

#numerical comparison: equality   
print("\nx == 10?") 
if x == 10:
    print("True")
else:
    print("False") 

print("\ny == 10?") 
if y == 10:
    print("True")
else:
    print("False") 
    
print("\nx == 3?") 
if x == 3:
    print("True")
else:
    print("False")     

print("\nx == y?") 
if x == y:
    print("True")
else:
    print("False")  

#numerical comparison: inequality    
print("\nx != 3?") 
if x != 3:
    print("True")
else:
    print("False") 
    
#numerical comparison: greater than or equal to     
print("\nx >= y?") 
if x >= y:
    print("True")
else:
    print("False")             

#numerical comparison: less than or equal to     
print("\nx <= y?") 
if x <= y:
    print("True")
else:
    print("False")       
    
#numerical comparison: and keyword
print("\nx > 3 and x < 10?") 
if (x > 3) and (x < 10):
    print("True")
else:
    print("False") 

#numerical comparison: or keyword
print("\nx > 3 or x < 10?") 
if (x > 3) or (x < 10):
    print("True")
else:
    False

# Test whether an item is in a list
vowels = ['a', 'e', 'i','o','u']
print("\nis vowel contains letter 'a'?")
if 'a' in vowels:
    print("True")
else:
    print("False")    
    
# Test whether an item is not in a list
print("\nis vowel contains letter 'p'?")
if 'p' in vowels:
    print("True")
else:
    print("False")   
    
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# Write an if statement to test whether the alien’s color is green. 
# If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails. 
# (The version that fails will have no output.)

alien_color = ["green", "yellow", "red"]

# Setting the color to green statically
if alien_color[0] == "green":
    print("\nYou just earned 5 points.")

#using inline if with logical operator  
print(f'{alien_color[0] == "yellow" and "You just earned 5 points." or ""}')

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

# Setting the color to green statically
if alien_color[0] == "green": 
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.") 
             
# Setting the color to red statically
if alien_color[0] == "red": 
    print("You just earned 5 points for shooting the alien.")
else:
    print("You just earned 10 points.\n") 
    
# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.

#iterate the list of colors and print the appropriate color alien
for color in alien_color:
    points = "" #variable to get how many points gained
    if color == "green":
        points = "5" 
    elif color == "yellow":
        points = "10"
    elif color == "red":
        points = "15"
    print(f"You just earned {points} points.")    
         
# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. 
# Set a value for the variable age, and then:
# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# If the person is age 65 or older, print a message that the person is an elder.

#create a variable that holds the age list
ages = list(range(1,70,2))
print(f"\nAges: {ages} \n")
#loop to each age in the list of ages
for age in ages:
    distinction = ""  #variable to distinguish age
    #age > 1 and < 2
    if age > 1 and age < 2:
        distinction = "baby"
    #age > 2 and < 4    
    elif age > 2 and age < 4:
       distinction = "toddler"
    #age > 4 and < 13    
    elif age > 4 and age < 13:
       distinction = "kid"
    #age > 13 and < 20    
    elif age > 13 and age < 20:
       distinction = "teenager"
    #age > 20 and < 65    
    elif age > 20 and age < 65:
       distinction = "adult"
    # above 65 
    else:
        distinction = "elder"
    print(f"Age is: {age}. Then this person is a { distinction.title() }")          
        
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent 
# if statements that check for certain fruits in your list.
# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

#list of fruits
fruits = ["apple","grapes","watermelon","orange", "guava", "bananas", "jackfruit"]
print(f"\nFruit list: {fruits}")

#list of favorite fruits
favorite_fruits = ["jackfruit", "grapes", "guava", "watermelon"]
print(f"Favorite fruit list: {favorite_fruits}")

for fruit in fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit.title()}!")
        