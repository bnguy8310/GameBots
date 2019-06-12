"""Test for my functions.

For each of my functions and some tests for my classes
"""
'''Imports'''
from functions_classes import *
from datascience import *
import numpy as np
import string
import random
import nltk
import time
import sys
##

def test_quit():
    
    assert type(quit('string')) == bool
    assert quit('quit') == False
    assert quit(123) == True
    
def test_typing():

    assert len(typing('string')) == len('string')
    assert typing('string') == 'string'
              
def test_difficulty_words():
    
    array = make_array('one','twoooo','threeeee')
    assert type(difficulty_words('easy', array)) == np.ndarray
    assert np.all(difficulty_words('easy', array) == make_array('one'))
    assert np.all(difficulty_words('medium', array) == make_array('one', 'twoooo'))
    assert np.all(difficulty_words('hard', array) == make_array('twoooo', 'threeeee'))
     
def test_stick_figure():
   
    assert stick_figure(3) == 3
    assert stick_figure(10) == None

def test_GameBots():
    
    gamebots = GameBots()
    gamebots.wins += 1
    assert type(gamebots.wins) == int
    assert gamebots.wins == 1
    assert gamebots.losses == 0
    

