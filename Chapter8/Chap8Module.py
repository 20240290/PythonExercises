# Joseph Patambag
# August 19, 2024

#Function declarations.

#Exercise 8.1
def display_message():
    """
    Print a string message on what we learn on this 
    chapter in the python crash course.
    """
    #print a simple message.
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
    #print the favorite book with book parameter.
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
    #msg variable to store message output
    msg = ""
    #Check condition if size returns the default value and as well the medium, should print the same output
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
    #country variable with inline if condition to check if country is equal to 'Canada' else return the country
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
    #returns the city and country values
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
    #returns album information
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
    #album variable that holds the album information.
    album = make_album(artist, album)
    if no_of_songs:
        #update album with no of songs value.
        album["songs"] = no_of_songs
    #returns album information    
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
    print("User albums! Type 'quit' to end the program.")
    while True:
        artist = input("Enter the song artist: \n")
        if artist == "quit": 
            break         
        album = input("Enter album title: \n")
        if album == "quit":
             break
        print(f"\nAlbum information is : {make_album(artist, album)} \n")
        
#Exercise 8.9

def show_messages(messages: list):
    """
    Method to display the list of messages.

    Parameters
    ----------
    messages: list
        Array of messages.

    Returns
    -------
    none
    """
    #Iterate each messages and print the value.
    for msg in messages:
        print(f"{msg} \n")

#Exercise 8.10

def create_message_list(messages: list,send_messages: list):
    """
    Method to display the list of messages.

    Parameters
    ----------
    messages: list
        Array of messages.
    send_message: list
        Empty list to store the messages.
    Returns
    -------
    Tupples
        Original list and send_messages list.

    """
    #Iterate messages parameter.
    while messages:
        #store message in the message variable.
        message = messages.pop(0)
        print(f"{message} \n")
        #add message to send_message parameter.
        send_messages.append(message)
    #returns a tuple value.    
    return (messages, send_messages)
    
#Exercise 8.11

def archived_messages(messages: list,send_messages: list):
    """
    Method to archive the list of messages.

    Parameters
    ----------
    messages: list
        Array of messages.

    Returns
    -------
    Tupples
        Original list and send_messages list.

    """
    #variable copy of messages parameter.
    messages_copy = messages[:]
    #call method 'create_message_list' to get a list of messages.
    create_messages = create_message_list(messages_copy, send_messages)
    #return a tuple value.
    return (messages, create_messages[1])

#Exercise 8.12

def make_me_a_sandwich(*items):
    """
    Method to create a sandwich one or more paramters.

    Parameters
    ----------
    items: variable
        Variable number of items to be added.

    Returns
    -------
    none

    """  
    #Add try exception to check values of the arguments.
    try:
        #itereate each items.
        for arg in items:
            print(f"You sandiwch has: {arg}")
        print("\n")    
    except TypeError as e:
        print(f"Error processing argument: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

#Exercise 8.13

def build_profile(first: str, last: str, **user_info):
    """
    Method to build a profile.

    Parameters
    ----------
    first: string
        User first name.
    last: string
        User last name.
    user_info: variable
        Variable parameter which will add more information of the user.

    Returns
    -------
    user_info: dictionary
        User information.

    """
    #user info argument set with firstname and lastname    
    user_info['fist_name'] = first
    user_info['last_name'] = last
    return user_info

#Exercise 8.14

def make_car(manufacturer: str, model: str, **car_props):
    """
    Method to show information of a specific car.

    Parameters
    ----------
    manufacturer: string
        Car manufacturer.
    model: string
        Car model.
    car_props: variable
        Variable parameter which will add more information of the car.

    Returns
    -------
    user_info: dictionary
        Car information.

    """
    #car variable that holds the manufacturer and model
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    #iterate car props and add it in the car dictionary
    for key,value in car_props.items():
        car[key] = value
    return car    

#Exercise 8.15

def printed_models(unprinted_designs: list, completed_models: list):
    """
    Method to show printed models.

    Parameters
    ----------
    unprinted_designs: list
        Unprinted design list.
    completed_models: list
        Completed models list.
    
    Returns
    -------
    completed_models: list
        Completed models list.

    """

    # Iterate unprinted designs and store it in completed_models and print it.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    return completed_models

#Exercise 8.16



#Exercise 8.17