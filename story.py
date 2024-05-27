# Modules
import emoji
from colorama import Fore, Style

# Colours for text
GRAY = Fore.LIGHTBLACK_EX
BROWN = "\033[38;2;139;69;19m" #print(BROWN + "text" + Style.RESET_ALL)
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE


# Functions
# 1. Welcome message
def welcome_msg():
    """
    Displays welcome message.

    Prints welcome content.
    """
    emoji_snail = emoji.emojize(":snail:")
    emoji_whale = emoji.emojize(":whale:")
    brown_dots = BROWN + "..." + Style.RESET_ALL
    blue_dots = BLUE + "..." + Style.RESET_ALL

    print("Welcome to the Snail Adventure\n") 
    print("Are you ready to embark on an adventure?\n") 
    print(f"{brown_dots}{emoji_snail}" + f" {blue_dots}{emoji_whale}\n") 

# 2. Get and validate ser's name
# get user's name
def get_username():
    """
    Gets name input from user.
    """
    # input() function takes all the input as a string only
    username = input("What's your name?\n")

    if validate_username(username):
        username = username.capitalize()
        print(f"{username} is a valid and capitalized username!\n")
   
    return username


# validate user's name
def validate_username(username):
    """
    Check user_name entered is a string and is not empty or just whitespace.
    Raises ValueError if data entered is not valid.
    """
    print(f"Validating username: {username} ...\n")
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    try:
        # check if if all characters in username string are alphabetic 
        if username.isalpha():
            print(f"Valid name: {username}")

        # check if username contains numbers or is empty
        elif username.isdigit() or username.strip() == "":
            raise ValueError("Username must contain only letters and be non-empty.\n")
        
        # check if username contains special characters
        elif any(c in special_characters for c in username):
            raise ValueError("Username must contain only letters, not special characters.\n")

    except ValueError as e:
        print(f"Invalid name: {e}\n")
        return False
    
    return True
    

# 3. Display story instructions
def display_instructions():
    """
    Prompts user to see instructions.

    Returns True for yes, otherwise False
    """



# read story (start adventure)
# show story introduction
# check user's choice
# redirect user to choosen story part
# end game -- show tracker info here
# read again
# display hint
# track user's page
# main function (call all functions)
def main():
    welcome_msg()
    get_username()

main()

# DICTIONARY
# dictionary for story (with text, pages number, and user options) to store and manage story data in key-value pairs
