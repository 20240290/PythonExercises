# Joseph Patambag
# August 19, 2024

#Function declarations.

#Exercise 8.1
def display_message():
    """
    Print a string message on what we learn on this 
    chapter in the python crash course.
    """
    print(f"Chapter 8 introduces another way of creating functions and modules to incorporate into the code. It makes code functionality neat and precise.\n")

#Exercise 8.2    
def favorite_book(book:str):
    """
    Print a string message of your favorite book.
    
    Args:
    ------
        book string: name of the book.
    """
    print(f"One of my favorite book is {book.title()}\n")

#Exercise 8.3 / 8.4
def make_shirt(message: str, size:str = "Large"):
    """
    Print a sentence summarizing the size of the shirt 
    and the message printed on it.

    Args:
    ------
        size (string optional): Size of the t-shirt. Defaults to "Large"
        content (string): Text design of the tshirt.
    
    Returns
    -------
    none   
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
    
    Args:
    -----
        city (str): name of the city
        country (str, optional): name of the country. Defaults to "Canada".
    """
    _country = f"{country == "Canada" and "Canada" or country}"  
    print(f"{city} is in {_country} \n")
    
    