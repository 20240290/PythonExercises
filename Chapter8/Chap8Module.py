# Joseph Patambag
# August 19, 2024

#Function declarations.

#Exercise 8.1
def display_message():
    """
    Print a string message on what we learn on this 
    chapter in the python crash course.
    """
    print(f"\nChapter 8 introduces another way of creating functions and modules to incorporate into the code. It makes code functionality neat and precise.\n")

#Exercise 8.2    
def favorite_book(book:str):
    """
    Print a string message of your favorite book.
    
    Parameters
    ----------
    book : string
       Name of the book.
    """
    print(f"One of my favorite book is {book.title()}\n")

#Exercise 8.3 / 8.4
def make_shirt(message: str, size:str = "Large"):
    """
    Print a sentence summarizing the size of the shirt 
    and the message printed on it.

    Parameters
    ----------
    size : string optional
        Size of the t-shirt. Defaults to "Large"
    content : str
        Text design of the tshirt.
    """
    msg = ""
    if size.lower() == "large" or size.lower() == "medium":
        msg = "I love Python!"
    else:
        msg = message
    
    print(f"Your t-shirt size is: {size.title()} and design content is: {msg.title()}\n")
    
#Exercise 8.5
def describe_city(city: str, country: str = "Canada"):
    """
    Print a simple sentence, such as Reykjavik is in Iceland

    Parameters
    ----------
    city : str
        A city name.
    country : str
        A country name.
    """
    _country = f"{country == 'Canada' and 'Canada' or country}"  
    print(f"{city.title()} is in {_country.title()} \n")
    
#Exercise 8.6
def city_country(city: str, country: str):
    """
    Method that accepts city and country and return the value. 

    Parameters
    ----------
    city : str
        A city name.
    country : str
        A country name.

    Returns
    -------
    str
       String format of city,name. ex: "Santiago, Chile".
    """
    return f"{city.title()},{country.title()}"

#Exercise 8.7

def make_album(artist: str, album: str):
    """
    Method that accepts the artist and album and return the value.

    Parameters
    ----------
    artist : str
        Artist name.
    album : str
        Album name.

    Returns
    -------
    dictionary
        album information in a dictionary
    """
    return {
        artist: album
    }

def make_album_with_songs(artist: str, album: str, no_of_songs: int = None):
    """
    Method that accepts the artist, album and no of songs and return the value.

    Parameters
    ----------
    artist : str
        Artist name.
    album : str
        Album name.
    no_of_songs: int
        No of songs in album.

    Returns
    -------
    dictionary
        album information in a dictionary
    """
    album = make_album(artist, album)
    if no_of_songs:
        album["songs"] = no_of_songs
    return album

#Exercise 8.8

def generate_user_album():
    """
    Method to generate a users album with artist and title and return the list of songs each user.

    Parameters
    ----------
    none

    Returns
    -------
    dictionary
        album information of the user in dictionary
    """
    print("User albums")
    while True:
        artist = input("Enter the song artist: \n")
        album = input("Enter album title: \n")

        


#Exercise 8.9

#Exercise 8.10

#Exercise 8.11

#Exercise 8.12

#Exercise 8.13

#Exercise 8.14

#Exercise 8.15

#Exercise 8.6

#Exercise 8.17