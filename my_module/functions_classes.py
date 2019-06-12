"""A collection of function and classes for doing my project."""

'''Imports'''

from datascience import *
import numpy as np
import string
import random
import nltk
import time
import sys


#function that will be used to stop loop
def quit(string):
    '''
    If given string is quit, returns False
    
    Parameters
    ---------------------- 
    Input 
        String
    
    Return
    ----------------------
    Output
        Boolean
    '''
    if string == 'quit':
        return False
    else:
        return True
    
# function that simulates typing
def typing(string):
    '''
    Simulate a human typing each letter at a time rather than all at once.
    
    Parameters
    ----------------------
    Input 
        String
    
    Return
    ----------------------
    Output
        Input string typed one letter at a time
    
    '''
    #prints each character of string one at a time 
    for char in string + '\n':
        time.sleep(1/30)
        sys.stdout.write(char)
        sys.stdout.flush()
    return string

#sort array of words with given difficulty
def difficulty_words(difficulty, array):
    '''
    Sorts an array of words according to difficulty differentiated with word lengths
    
    Parameters
    ----------------------
    Inputs 
        Difficulty has to be 'easy','medium', or 'hard'
        Array of words
    
    Return
    ----------------------
    Output
        Array of words with word lengths greater than minimum and less than maximum lengths according to difficulty
    '''
    #setting boundaries for word lengths according to difficulty
    if difficulty == 'easy':
        min_length = 0 
        max_length = 3
    elif difficulty == 'medium':
        min_length = 3
        max_length = 6
    elif difficulty == 'hard':
        min_length = 6
        max_length = 10
    
    #new array containing sorted words
    sorted_words = make_array()
    for word in array:
        if min_length <= len(word) <= max_length:
            #appending words that are True to statement
            sorted_words = np.append(sorted_words, word) 
    return sorted_words

#imaginary stick figure used for hangman
def stick_figure(number_of_wrong):
    '''
    Prints stages of stickfigure based on incorrect guesses
    
    Parameters 
    ----------------------
    Input
        Number of incorrect guesses
    
    Return 
    ----------------------
    Output
        Stages of stick figure
    '''
    if number_of_wrong == 0:
        print('[             ]')
        print('[             ]')
        print('[             ]')
        print('[             ]')
        print('You have 7 tries left!')
        return 0
    elif number_of_wrong == 1:
        print('[      |      ]')
        print('[             ]')
        print('[             ]')
        print('[             ]')
        print('You have 6 tries left!')
        return 1
    elif number_of_wrong == 2:
        print('[      |      ]')
        print('[      o      ]')
        print('[             ]')
        print('[             ]')
        print('You have 5 tries left!')
        return 2
    elif number_of_wrong == 3:
        print('[      |      ]')
        print('[      o      ]')
        print('[      |      ]')
        print('[             ]')
        print('You have 4 tries left!')
        return 3
    if number_of_wrong == 4:
        print('[      |      ]')
        print('[      o      ]')
        print('[     /|      ]')
        print('[             ]')
        print('You have 3 tries left!')
        return 4
    elif number_of_wrong == 5:
        print('[      |      ]')
        print('[      o      ]')
        print('[     /|\     ]')
        print('[             ]')
        print('You have 2 tries left!')
        return 5
    elif number_of_wrong == 6:
        print('[      |      ]')
        print('[      o      ]')
        print('[     /|\     ]')
        print('[     /       ]')
        print('You have 1 tries left!')
        return 6
    elif number_of_wrong == 7:
        print('[      |      ]')
        print('[      o      ]')
        print('[     /|\     ]')
        print('[     / \     ]')
        print('You have 0 tries left!')
        return 7
    else:
        return None
    
"""A collection of Classes for doing my project."""
#making a class that is the main menu for each of the bots
class GameBots():
    '''
    Class that is the base for potential game bots 
    ----------------------
    Attributes : self.wins, self.losses
    ----------------------
    Methods : view_records()
    '''
    
    #attributes which count the number of wins and losses 
    def __init__(self):
        self.wins = 0
        self.losses = 0
    
    #method that shows number of wins and losses
    def view_records(self):
        print("You have won " + str(int(self.wins)) + " times in this game!") 
        print("You also have lost " + str(int(self.losses)) + " times in this game D:")
    
    

#making a game bot that has the features of the class GameBots
class HangMan(GameBots):
    '''
    Main chatbot that plays the game HangMan.
    ----------------------
    Atrributes : takes Gamebots attributes, self.wins, self.losses
    ----------------------
    Methods : start()
    '''
    #hangman's wins and losses
    def __init__(self):
        super().__init__()

    #method throughout the game
    #starting the game
    
    def start(self):
        typing("The game is going to start, you may quit anytime you want by inputting 'quit'.")
        #pauses chatbot to simulate a real conversation
        time.sleep(1)
        
        #while loop to continue game until game is done or user wants to quit
        game_is_going = True
        while game_is_going:
            typing('Thank you for choosing HangMan! What is your name?')
            #wait 1 seconds
            time.sleep(1)
            
            input_name = input('Enter Name: ')
            
            #wait 1 seconds
            time.sleep(1)
            
            #breaks loop when user wants to quit
            game_is_going = quit(input_name.lower())
            if game_is_going == False:
                break
            
            #wait 1 seconds
            time.sleep(1)
            
            #Greets the user and asks for diffculty
            typing("Hello " + input_name + "!")
            
            #wait 1 seconds
            time.sleep(1)
            while game_is_going:
                difficulty = typing("Now, what difficulty would you like " + input_name.title() + '?')
                difficulty = input('Easy, Medium, Hard: ')
                if difficulty.lower() not in ['easy','medium','hard']:
                    typing('Please input a difficulty')
                else:
                    break
           
            #breaks loop when user wants to quit
            game_is_going = quit(difficulty.lower())
            if game_is_going == False:
                break
            
            
            #wait 1 second
            time.sleep(1)
            typing("Please give me a few moments to start the game...")
            
            #printing sentences that imagine bot starting up the game
            for seconds in np.arange(5):
                
                if seconds == 0:
                    time.sleep(1)
                    typing("Grabbing necessary functions...")
                    #getting possible words according to difficulty
                    list_of_words = Table().read_table('../ProjectTemplate/my_module/words.csv')
                    
                elif seconds == 1:
                    time.sleep(1)
                    typing("Picking a random word...")
                    words_in_play = difficulty_words(difficulty.lower(), list_of_words.column('Words'))
                        
                elif seconds == 2:
                    time.sleep(1)
                    typing("Almost done !")
                    official_word = np.random.choice(words_in_play).lower()
                    
                elif seconds == 3:
                    time.sleep(1)
                    typing("Starting now !")
                
                else:
                    time.sleep(3)
           
            #start of the actual game  
            print('----------------------------------------------------------------')
            time.sleep(1)
            
            #game word substituted by underscores
            game_word = '_' * len(official_word)
            number_of_incorrect = 0
            letters_used = []
            
            time.sleep(1)
            #loop over guesses 
            while game_is_going: 
                stick_figure(number_of_incorrect)
                
                #end of game if too many incorrect guesses
                if number_of_incorrect == 7:
                    self.losses += 1
                    typing('You have lost this game')
                    typing('The word was ' + official_word)
                    break
                    
                print(game_word)
                print('Letters used: ', end = ' ') 
                print(letters_used)
                
                #input letter guess
                while True:
                    guess = input('What is your guess?: ').lower()
                   
                    #breaks loop when user wants to quit
                    game_is_going = quit(guess)
                    if game_is_going == False:
                        break
                    
                    #if user guesses same letter
                    elif guess in letters_used:
                        typing('You already guessed that word! Please pick another letter!')
                        break
                        
                    #tells user if input is incorrect
                    if len(guess) != 1:
                        typing('Please input only one letter at a time!')
                        continue
                    elif guess in string.punctuation:
                        typing('Please input a letter!')
                        continue
                    elif guess == ' ':
                        typing('Please input a letter!')
                        continue
                    elif type(guess) is not str:
                        typing('Please input a letter!')
                        continue
                
                    letters_used += guess
                
                    #if user guesses a correct letter
                    if guess in official_word:
                        typing('Correct !')
                        index = official_word.find(guess)
                        game_word = game_word[:index] + guess + game_word[index + 1:]
                        break
                
                    #if user guess wrong letter
                    else:
                        typing('Uh oh, try again')
                        number_of_incorrect += 1
                        break
            
                #win conditions
                if '_' not in game_word:
                    self.wins += 1
                    break
                
                #wait 1 second
                time.sleep(1)
                
            break
        
        time.sleep(1)
        print('----------------------------------------------------------------')
        
        #uses method from GameBot and prints number of wins and losses
        self.view_records()
        time.sleep(1)
        typing('Thank you for playing me! Have a nice day!')
        