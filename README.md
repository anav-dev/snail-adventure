# Snail Adventure
![Snail Adventure](https://github.com/anav-dev/snail-adventure)
Snail Adventure is a Python text-based adventure game which runs on Heroku.

Users can move through different scenarios within a single setting, based on their input. The game provides descriptions for each scenario. 

Users can only move in certain directions between the scenarios. Hints will be provided if required by users, as a method for guiding them in the correct direction and helping them avoid mistakes. Hints are brief descriptions provided, aiming to assist users in entering the correct information. 

The story adventure will be tracked to check how far an user has gone in the story. 

**Click here to see live site**: [Snail Adventure]()

## How to Interact with the Game

  Snail Adventure is based on "The Snail and the Wale" story. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/The_Snail_and_the_Whale) .

  In this version, the user the user enters their name and the story introduction is displayed.

  Users can see the different story scenarios and move in certain directions between the scenarios depending on their choice.

  The computer will provide hints and error messages when required.

  The user will receive information on how far the user has read in the story.

### User Interactions

  Following the essence of the *Choose Your Own Adventure series*, same steps will be folowed as follows:

    1. The story begins on page 1.
    2. The user reads the page.
    3. A decision point is displayed to the user.
    4. The user chooses an option.
    5. Based on the user's choice, they navigate to the corresponding page number.
    6. Repeat steps 2 to 4 until user reaches end of the story.

  <details>
  <summary>Click here to visualize user interactions flow chart</summary>
  <br>
    
  ![User Interactions](https://github.com/anav-dev/snail-adventure/blob/main/docs/features/user-interactions.jpeg)

  </details>

## User Experience

- __User Stories__
  
  **As a user I would like to:**

    >Be able to access the story so that I can read it.
    >Be able to choose the main character's next step so that I can decide the story's direction.
    >Be able to see error messages so that I can understand when and why something went wrong.
    >Be able to receive a hint so that I can have guidance. 



## Design
- __Flow Charts__

  Both the story's and the logic flow charts was created by using [Lucidchart.com/](https://www.lucidchart.com/)

  This story's flow chart represents the story of the snail adventure game, showing different scenarios depending on user's choice.
  
  <details>
  <summary>Click here to see story's flow chart</summary>
  <br>
    
  ![Story Flow](https://github.com/anav-dev/snail-adventure/blob/main/docs/features/adventure-mapout.jpeg)

  </details>

  This logic's flow chart represents the things the program needs to do and the logic path the program needs to take.
  
  <details>
  <summary>Click here to see logic's flow chart</summary>
  <br>
    
  ![Logic Flow](https://github.com/anav-dev/snail-adventure/blob/main/docs/features/logic-flow.png)

  </details>



- __Colour Palettes__ 

  The below HEX codes provide a close representation of the colors used in the Python module Colorama.

  ![Colour Scheme](https://github.com/anav-dev/snail-adventure/blob/main/docs/features/color-scheme.jpg)

  Red and green colors are used to highlight recommended and not recommended choices, respectively, as well as to guide users when entering data. This enhances user experience by providing clear visual cues.


## Features

- __Story Page__

- __Choices__

- __Hint__

- __Future Features__


## Technology

## Testing

### Bugs

- __Python: Not Recognized Command__

    When using the command `os.system("clear")` to clear the screen, the following error appears as the command was not recognized. 
    
    <details>
    <summary>Click here to see error and faulty code</summary>
    <br>
    
    ![Command Error](https://github.com/anav-dev/snail-adventure/blob/main/docs/test/command-error.jpg)
    ![Faulty Code](https://github.com/anav-dev/snail-adventure/blob/main/docs/test/command-error-code.jpg)

    </details>
    
    The error arose because the `clear` command is specific to Unix-based systems like Linux and macOS, and it's not recognized by the Windows command prompt. Error solved by using correct command for Windows systems, as follows: `os.system("cls")`.

- __Python: Colorama Behavior__

    After validating the username, any following printed lines will adopt the colour of the preceding line, rendering them in gray.

    <details>
    <summary>Click here to see issue</summary>
    <br>
    
    ![Colorama Issue](https://github.com/anav-dev/snail-adventure/blob/main/docs/test/colorama-issue.jpg)

    </details>

    Setting the error message colour to white and resetting all styles after printing that line resolved the unexpected behavior.

    <details>
    <summary>Click here to see updated code</summary>
    <br>
    
    ![Code Fixed](https://github.com/anav-dev/snail-adventure/blob/main/docs/test/colorama-issue-code.jpg)

    </details>

- __Python TypeError: Unhashable Type__
  
    The error TypeError: unhashable type: 'list' in Python occurs when trying to use a list as a hash argument although a list is an unhashable object. For instance, using a list as a key in a Python dictionary will result in an error because dictionaries require keys to be hashable data types. 
    
    <details>
    <summary>Click here to see error</summary>
    <br>
    
    ![Error](https://github.com/anav-dev/snail-adventure/blob/main/docs/test/typeerror-unhashable.jpg)

    </details>
    
    This issue was addressed by correcting the way the input function was used and ensuring that the user's input is validated against the list of choices (choices) using a while loop.

    <details>
    <summary>Click here to see updated function</summary>
    <br>
    
    ![Code Fixed](https://github.com/anav-dev/snail-adventure/blob/main/docs/test/typeerror-unhashable-code.png)

    </details>



## Deployment

This project was deployed from the main branch using [Heroku platform](https://www.heroku.com/).

**Steps:**
  - Clone this repository: `https://github.com/anav-dev/snail-adventure.git`
  - Create a new Heroku App.
  - Set the buildbacks to `Python` and `NodeJs` in that order.
  - Link the Heroku App to the repository.
  - Click on Deploy.

## Credits

**References**
- Wikipedia: [The Snail and the Whale Story](https://en.wikipedia.org/wiki/The_Snail_and_the_Whale)
- Kyle Lierer Github: [Text Adventure Tutorial](https://github.com/Kyle-L/Text-Adventure-Tutorial?tab=readme-ov-file#how-will-the-user-interact-with-the-game)
- Flow Chart Application: [Lucidchart.com/](https://www.lucidchart.com/)
- Colour Palettes: [Coolors.co](https://coolors.co/)


**Troubleshooting**
- MDN Documentation: [MDN Docs](https://developer.mozilla.org/en-US/) 
- W3Schools: [W3Schools.com](https://www.w3schools.com/) 
- StackOverflow: [Stackoverflow.com](https://stackoverflow.com/)
- CI Python Linter: [CI Python Linter](https://pep8ci.herokuapp.com/)

  
**Support & Advice**
- Mentor: Alan Bushell
- Code Institute | Slack Community

