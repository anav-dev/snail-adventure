# Modules
import emoji
from colorama import Fore, Style
from justifytext import justify
import time # Importing time module to use sleep function
import os # Importing os module to use system function
import sys # Importing sys module to use stdout attribute

# Import data from story_file.py
from story_file import snail_story


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

answer_yes = ("yes", "y", "ye", "yep", "ok", "okay")
answer_no = ("no", "n", "not", "nop", "nope")

query_instr = "would you like to see the instructions?"
query_adv = "are you ready to start the adventure?"
query_choice = "what's your next move?"
query_reset = "do you prefer to restart this adventure?"
query_hint = "Hint needed? (yes/no)"


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
        print(GREEN + f"{username_validated} is a valid username!\n" + Style.RESET_ALL) 
   
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
            #print(f"{blue_dots}{emoji_whale}\n")
            print()

        # check if username contains numbers or is empty
        elif username.isdigit() or username.strip() == "":
            raise ValueError("Username must contain only letters and be non-empty.\n")
        
        # check if username contains special characters
        elif any(c in special_characters for c in username):
            raise ValueError("Username must contain only letters, not special characters.\n")

    except ValueError as e:
        print(RED + f"Invalid name: {e}\n" + Style.RESET_ALL)
        get_username()
        return False        
    
    return True
    
# 3. Functions for displaying instructions
def print_instructions():
    """
    Prints story instructions.
    """
    typing_print("\nLoading instructions, please wait...\n", GRAY)
    pause_and_clear()

    #ASCII generator source: https://manytools.org/hacker-tools/ascii-banner/
    print(BROWN+ r'''
                ════════════════ Instructions ═════════════════════ 
    ''')
 
    instructions = "Snail Adventure is a text-based game where you will engage in a story-driven experience.\nYou will encounter different scenes, challenges, and offer choices.\nBy selecting a choice, such as “help”, “take action,” or “accept offer”,\nyou will move to the next corresponding chapter, advancing the story based on your decisions.\n"
    instructions_justified = (justify(instructions, 85))
    
    for i in instructions_justified:
        print("\n" + BROWN + i + Style.RESET_ALL + "\n")

    print(BROWN + r'''
                ═══════════════════════════════════════════════════  
    ''' + Style.RESET_ALL)

    # add question here (ready to start your adventure?)

# 4. Function for yes/no question 
def ask_question(username_validated, query):
    """
    Receives the validated username and a query.
    Prompts user to answer a question.

    Args:
        string: username validated.
        string: query.
    """
    try:
        #print(f"{username_validated}, would you like to see the instructions? (yes/no)\n")
        #typing_print(f"{username_validated}, would you like to see the instructions? (yes/no)\n", WHITE) 
        typing_print(f"{username_validated}, {query} (yes/no)\n", WHITE)
        ask_question_answer = input().strip().lower()
        
        # if yes answered
        if ask_question_answer in answer_yes:
            #print("yes answered")
            # check if the second paramenter matches a specific query; then run corresponding function based on second paramenter
            if query == query_instr:
                print_instructions()
                ask_question(username_validated, query_adv)
            elif query == query_adv:
                #print("query_adv_yes")
                typing_print(f"Loading story, {username_validated} please wait...\n", GRAY)
                pause_and_clear()
                # ** story starts here **
                story_flow(snail_story)
            elif query == query_reset:
                print("query_reset_yes")
            else:
                print("Query not recognized.")
        # if no answered
        elif ask_question_answer in answer_no:
            # check if the second paramenter matches a specific query; then run corresponding function based on second paramenter
            if query == query_instr:
                ask_question(username_validated, query_adv)
            elif query == query_reset:
                print("query_reset_no")
            else:
                print("Query not recognized.")
            
        # else
        else:
            print(RED + "Please enter a right answer (yes/no) \n" + Style.RESET_ALL)
            ask_question(username_validated, query)
    except ValueError as e:
        print("Error")


# 5. Function to access data from story_file.py file
def access_story_data(snail_story, page_number):
    """
    Accesses 'Text', 'Options', 'Hint' data for a specific page number.

    Args:
        data (dict): data structure imported from story_file.py
        page_number (int): page number for which data needs to be accesed.

    Returns:
        tuple: containing the data for the given page number. 
                (if page number is not found, returns None) 
    """
    # get data for specific page number using get method
    page_data = snail_story.get(page_number)

    if(page_data):
        # if page data exists, get text, options and hint
        text = page_data.get('Text', [])
        options = page_data.get('Options', [])
        hint = page_data.get('Hint', [])
        return text, options, hint
    else:
        # return none if page number is not found
        return None, None, None


# 6. Function to display page text
def print_text(stringlist: list):
    """
    Prints each line of text one by one and pauses for a short time after each line.

    Args:
        lines (list): A list of strings, where each string is a line of text to display.
    """
    if stringlist == text: 
        for line in stringlist:     
            print(WHITE + line + Style.RESET_ALL) # Print the line with a newline character at the end
            time.sleep(0.1) # Pause for 0.1 seconds
        print() # Print an empty line for better readability

    elif stringlist == options:
        for i, (option_text, option_page) in enumerate(options): # enumerate function provides a counter to the loop
            print(f"{i + 1}.{option_text} || Go to page: {option_page}")

    elif stringlist == hint:
        if hint:
            user_hint_answer = input(f"{query_hint}")

            if user_hint_answer in answer_yes:  
                print(hint[0])
            elif user_hint_answer in answer_no:
                print("no hint needed")
                
            
        
        
        


# 7. Get and validate user's choice 
def get_choice(choices: list) -> str: # Return type annotation added here "-> str" so Python will enforce that the return value must be a string
    """
    Prompts user to choose a valid option.
    Validates choice.
    Return input entered as a string if that input is found within valid_choice list

    Args:
        valid_choice (list): A list of strings, the possible choices to make.

    Returns:
        str:  Choice entered if valid; "Invalid choice" if input not found in the valid_choice list.
    """
    # retrieve options text and page
    option_one = choices[0][0]
    option_one_page = choices[0][1]

    option_two = choices[1][0]
    option_two_page = choices[1][1]

    while True:
        user_choice = input(f"{username_validated}, {query_choice}\n\n{option_one}\n{option_two}\n")  

        if user_choice in choices:
            print(GREEN + "Valid choice" + Style.RESET_ALL)
            #return user_choice
        else:
            print(RED + "Invalid choice. Please choose from the provided options." + Style.RESET_ALL)     



# 8. Get next page | Redirect user to choosen story page
#def get_next_page():



# global variables used on below functions
curr_page = 1 # set current page
text, options, hint = access_story_data(snail_story, curr_page) # retrieve data from snail_story file


# 9. Story flow
def story_flow(story):
    # 9.1. print curr page text
    print_text(text)
    
    # 9.2. get user choice and display hint if needed
    get_choice(options)
    #print_text(options)
    #print_text(hint)
        
    # 9.3. check user input
    # 9.4. display next page according to user choice


# reset adv, read story again
# track user's page
# end game -- show tracker info here + option to reset adv


# main function (call all functions)
def main():
    welcome_msg()
    get_username()
    ask_question(username_validated, query_instr)

main()


