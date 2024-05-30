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
    
  ![Logic Flow](https://github.com/anav-dev/snail-adventure/blob/main/assets/docs/features/)

  </details>



- __Colour Palettes__

  In the Hint section, a redish colour `#9a031e` and a greenish colour `#2c6e49` were used to highlight advisable and not recommended choices respectively as well as to enhance the user experience by improving visual clarity.

  ![Colour Scheme](https://github.com/anav-dev/snail-adventure/blob/main/docs/features/color-scheme.jpg)


## Features

- __Story Page__

- __Choices__

- __Hint__

- __Future Features__


## Technology

## Testing

### Bugs

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

  
**Support & Advice**
- Mentor: Alan Bushell
- Code Institute | Slack Community

