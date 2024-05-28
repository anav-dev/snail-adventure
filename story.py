# Modules
import emoji
from colorama import Fore, Style
from justifytext import justify

# Colours for text | Source: https://pypi.org/project/colorama/
GRAY = Fore.LIGHTBLACK_EX
BROWN = "\033[38;2;139;69;19m" #print(COLOUR + "text" + Style.RESET_ALL)
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE

# Global variables declaration
emoji_snail = emoji.emojize(":snail:")
emoji_whale = emoji.emojize(":whale:")
brown_dots = BROWN + "..." + Style.RESET_ALL
blue_dots = BLUE + "..." + Style.RESET_ALL
username_validated = ""


# Functions
# 1. Welcome message
def welcome_msg():
    """
    Prints welcome message.
    """
    print("Welcome to the Snail Adventure\n") 
    print("Are you ready to embark on an adventure?\n") 
    print(f"{brown_dots}{emoji_snail}\n") 

# 2. Get and validate ser's name
# get user's name
def get_username():
    """
    Gets name input from user.

    Returns username.
    """
    # input() function takes all the input as a string only
    username = input("What's your name?\n")

    if validate_username(username):
        global username_validated
        username_validated = username.capitalize()
        print(f"{username_validated} is a valid username!\n") 
   
    return username_validated


# validate user's name
def validate_username(username):
    """
    Check username entered is a string and is not empty or just whitespace.
    Raises ValueError if data entered is not valid, and returns False.

    Returns True if data is valid.
    """
    print(f"Validating username: {username} ...\n")
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    try:
        # check if if all characters in username string are alphabetic 
        if username.isalpha():
            print(f"{blue_dots}{emoji_whale}\n")

        # check if username contains numbers or is empty
        elif username.isdigit() or username.strip() == "":
            raise ValueError("Username must contain only letters and be non-empty.\n")
        
        # check if username contains special characters
        elif any(c in special_characters for c in username):
            raise ValueError("Username must contain only letters, not special characters.\n")

    except ValueError as e:
        print(f"Invalid name: {e}\n")
        get_username()
        return False        
    
    return True
    

# 3. Display story instructions
def display_instructions():
    """
    Prints story instructions.
    """
    instructions = "Snail Adventure is a text-based game where you will engage in a story-driven experience.\nYou will encounter different scenes, challenges, and offer choices.\nBy selecting a choice, such as “help”, “take action,” or “accept offer”,\nyou will move to the next corresponding chapter, advancing the story based on your decisions.\n"
    instructions_justified = (justify(instructions, 85))
    
    for i in instructions_justified:
        print("\n" + BROWN + i + Style.RESET_ALL + "\n")

# 4. Yes or No Question 
def query_instructions(username_validated):
    """
    Receives the validated username.
    Prompts user to see story instructions.
    """
    answer_yes = ("yes", "y", "ye", "yep", "ok", "okay")
    answer_no = ("no", "n", "not", "nop", "nope")

    try:
        print(f"{username_validated}, would you like to see the instructions? (yes/no)\n")
        query_instructions_answer = input().strip().lower()
        
        # if yes answered
        if query_instructions_answer in answer_yes:
            #print("yes answered")
            display_instructions()
        # if no answered
        elif query_instructions_answer in answer_no:
            print("no answered --> call function to start story")
        # else
        else:
            print("Please enter a right answer (yes/no) \n")
    except ValueError as e:
        print("Error")
  






# read story (start adventure)
# check user's choice
# display hint
# redirect user to choosen story part
# end game -- show tracker info here
# read again
# track user's page
# main function (call all functions)
def main():
    welcome_msg()
    get_username()
    query_instructions(username_validated)

main()

# DICTIONARY
# dictionary for story (with text, pages number, and user options) to store and manage story data in key-value pairs
