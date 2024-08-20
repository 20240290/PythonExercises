# Joseph Patambag
# August 19, 2024

#Module import
import Chap8Module as module

# 8-7. Album: Write a function called make_album() that builds a 
# dictionary describing a music album. The function should take in an 
# artist name and an album title, and it should return a dictionary 
# containing these two pieces of information. Use the function to make 
# three dictionaries representing different albums. Print each return value 
# to show that the dictionaries are storing the album information correctly.

print(f"{module.make_album('Man in a mission/Milet','Kizuna no Kizeki')}\n")
print(f"{module.make_album('My First Story/Hyde','Mugen')}\n")
print(f"{module.make_album('OneRepublic','Nobody')}\n")

# Use None to add an optional parameter to make_album() that allows you to 
# store the number of songs on an album. If the calling line includes a 
# value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number 
# of songs on an album.

print(f"{module.make_album_with_songs('My First Story/Hyde','Mugen', 5)}\n")
print(f"{module.make_album_with_songs('OneRepublic','Nobody')}\n")
print(f"{module.make_album_with_songs('Man in a mission/Milet','Kizuna no Kizeki', 10)}\n")