# GameBots
GameBots code that can be the foundation to games in the form of a chat bot <br>
#### Below is the same description that is found in the Jupyter Notebook

### GameBots Description <br>
This project primarily focuses on a Bot that simulates a Hang Man game using styles of a chatbot in the form of a class. 
There is also an initial GameBot class that can be the base of several other games. I was inspired by the idea to make a chatbot 
related project from my class at UCSD COGS18 Introduction to Python class in Assignment 3. As a result, I started from scratch and 
went on this route to create a Hang Man game because I believed that it would challenge and prove my progress in Python. Also, this 
is a game which I enjoyed playing when I was young. The HangMan bot that I have written is simple and basic, which could definitely 
be improved in the future with more experience.

A description of the code each step of the way using GameBots to create the HangMan bot: <br>
At first I decided to make to make the class GameBots() to be the foundation and the set up for potential games. It has two attributes 
that holds the number of wins and losses. It also has a method where it prints the number of wins and losses when called.

I then went through and decided to make the HangMan() class that takes the instances of GameBots. After that, I made the method 
to start the game which is HangMan().start() which resembles a start button in a menu. The whole bot is a in the form of a while 
loop. I started with an outline of the most basic chatbot where it starts by saying asking the user's name and breaks after saying 
"Hello (user's name)". Following that, I defined functions to be the components of the HangMan game. I used my knowledge of arrays a
nd tables to create a function that picks random words from a list of words based on the difficulty the user picks. Next, I formed the 
hangman stick figure to be represented by strings in brackets, lines, and slashes. I also added code after every input to break the loop 
and quit the game if the user ever inputs "quit". Finally, I attached everything in order to form the Hang Man game.
