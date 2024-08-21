# Joseph Patambag
# August 19, 2024

#Module import
from Chap8Module import build_profile

# 8-13. User Profile: Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first 
# and last names and three other key-value pairs that describe you.

user = build_profile('John', 
                     'Doe', 
                     age = '35', 
                     address = '32 Reed St, Mary Land US 2343534', 
                     profession = 'Software Engineer' )

print(f"User information is: {user} \n")