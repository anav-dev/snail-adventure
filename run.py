# Modules
import emoji
from colorama import Fore, Style
from justifytext import justify
import time # Importing time module to use sleep function
import os # Importing os module to use system function
import sys # Importing sys module to use stdout attribute


# Colours for text | Source: https://pypi.org/project/colorama/  
BLACK = Fore.BLACK
BLUE = Fore.BLUE
BROWN = "\033[38;2;139;69;19m"
CYAN = Fore.CYAN
GRAY = Fore.LIGHTBLACK_EX
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
RED = Fore.RED
WHITE = Fore.WHITE


# Global variables declaration
emoji_snail = emoji.emojize(":snail:")
emoji_whale = emoji.emojize(":whale:")
brown_dots = BROWN + "..." + Style.RESET_ALL
blue_dots = BLUE + "..." + Style.RESET_ALL
username_validated = ""


# Functions for typing text effect; code adapted from: https://www.101computing.net/python-typing-text-effect/
# 1. Clear screen
def clear_screen():
    """
    Clears screen.
    """
    os.system("cls") #for windows CMD use "cls", for Unix/MAC/Linux use "clear"

# 2. Typing print
def typing_print(text, color): #second paramenter is color to fix color issue
    """
    Creates typing effect.
    """
    for character in text:
        sys.stdout.write(color + character)
        sys.stdout.flush()
        time.sleep(0.05)

# 3. Pause and call clear screen
def pause_and_clear():
    """
    Clears screen after a brief pause.
    """
    time.sleep(1.5)
    clear_screen()


# Functions for story 
# 1. Welcome message
def welcome_msg():
    """
    Prints welcome message and snail emoji.
    """

    typing_print("\nWelcome to Snail Adventure\n", WHITE) 
    print(f"\n{brown_dots}{emoji_snail}\n") 

# 2. Get and validate user's name
# 2.1. Get username
def get_username():
    """
    Gets name input from user.

    Returns:
        string: username.
    """
    # input() function takes all the input as a string only
    username = input("What's your name?\n")

    if validate_username(username):
        global username_validated
        username_validated = username.capitalize()
        print(f"{username_validated} is a valid username!\n") 
        typing_print("\nPlease wait, clearing screen ...\n", GRAY)
        # BUFHERE AFTER THIS LINE EVERYTHING IS GRAY COLOUR -> FIX
        time.sleep(3)
        clear_screen()
   
    return username_validated

# 2.2. Validate username
def validate_username(username):
    """
    Check username entered is a string and is not empty or just whitespace.
    Raises ValueError if data entered is not valid, and returns False.

    Args:
        string: username entered.

    Returns:
        True: if data is valid.
    """
    typing_print(f"\nValidating username: {username} ...\n", GRAY)
    special_characters = "!@#$%^&*()-+?_=,<>/"
    
    try:
        # check if if all characters in username string are alphabetic 
        if username.isalpha():
            print(f"\n{blue_dots}{emoji_whale}\n")

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
    
# 3. Functions for displaying instructions
def display_instructions():
    """
    Prints story instructions.
    """
    typing_print("\nLoading instructions, please wait...\n", GRAY)
    time.sleep(3)
    clear_screen()

    instructions = "Snail Adventure is a text-based game where you will engage in a story-driven experience.\nYou will encounter different scenes, challenges, and offer choices.\nBy selecting a choice, such as “help”, “take action,” or “accept offer”,\nyou will move to the next corresponding chapter, advancing the story based on your decisions.\n"
    instructions_justified = (justify(instructions, 85))
    
    for i in instructions_justified:
        print("\n" + BROWN + i + Style.RESET_ALL + "\n")

    # add question here (ready to start your adventure?)

# 4. Function for yes/no question 
def query_instructions(username_validated):
    """
    Receives the validated username.
    Prompts user to see story instructions.

    Args:
        string: username validated.
    """
    answer_yes = ("yes", "y", "ye", "yep", "ok", "okay")
    answer_no = ("no", "n", "not", "nop", "nope")

    try:
        #print(f"{username_validated}, would you like to see the instructions? (yes/no)\n")
        typing_print(f"{username_validated}, would you like to see the instructions? (yes/no)\n", WHITE) 
        query_instructions_answer = input().strip().lower()
        
        # if yes answered
        if query_instructions_answer in answer_yes:
            #print("yes answered")
            display_instructions()
        # if no answered
        elif query_instructions_answer in answer_no:
            #print("no answered --> call function to start story")
            typing_print("Loading story, please wait...\n", GRAY)
            time.sleep(3)
            clear_screen()
            lines_test = ["Hello world", "This is a test.", "Some text."]
            display_page_text(lines_test)
        # else
        else:
            print("Please enter a right answer (yes/no) \n")
    except ValueError as e:
        print("Error")

# 5. Function to display page text
def display_page_text(lines):
    """
    Displays each line of text one by one and pauses for a short time after each line.

    Args:
        lines (list): A list of strings, where each string is a line of text to display.
    """
    for line in lines:     
        print(line) # Print the line with a newline character at the end
        time.sleep(0.1) # Pause for 0.1 seconds
    
    print() # Print an empty line for better readability


# 6. Get user's choice 


# 7. Get next chapter | Redirect user to choosen story page


# 8. Story flow


# display hint
# end game -- show tracker info here
# read again
# track user's page

# main function (call all functions)
def main():
    welcome_msg()
    get_username()
    query_instructions(username_validated)
    #lines_test = ["Hello world", "This is a test.", "Some text."]
    #display_page_text(lines_test)

main()


