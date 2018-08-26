'''
Author: Mark Huff
Date: 8/26/18
'''

import random

class Hangman:

    def __init__(self):
        deathDictionary = {1: 'Noose Stand', 2: 'Head', 3: 'Body',
                            4: 'Left Hand', 5: 'Right Hand',
                            6: 'Left Leg', 7: 'Right Leg', 8: 'Noose'}

        wordDictionary = {"python", "list", "dictionary", "set",
                            "tuple", "docstrings", "json"}

        self.game(deathDictionary, wordDictionary)

    def game(self, deathDictionary, wordDictionary):
        '''
        :param deathDictionary: Has the parts of hangman picture.
        :param wordDictionary: Contains words that can be used in a game.
        :return: Nothing
        '''

        print("\nWelcome to Hangman corner. Hint: all words are in lower case.")
        again = ''
        misses = 0
        deathString = ''

        '''Selects a word from the word dictionary.'''
        word = random.choice(list(wordDictionary))

        '''Determines the size of the word selected.'''
        length = int(len(word))

        '''
        Sets the string of question marks.
        Note: Shows the player the word length.
        '''
        playersKnows = '?' * int(length)

        '''
        Game goes until the word is uncovered or 8 letters 
        not in word are guessed.
        '''
        while '?' in playersKnows and misses < 8:

            '''Prints what the player knows so far about the word.'''
            print(playersKnows)

            '''Asks player to guess a letter in the word.'''
            guess = ''
            while len(guess) != 1 or not guess.isalpha():
                guess = input("What letter do you want to guess? ").lower()

            '''
            If the letter is not in the word then another part of hangman
            picture is created.
            '''
            if guess not in word:
                print("Letter is not in word.")
                misses += 1
                deathString += " " + deathDictionary[misses]
                print("Added " + deathDictionary[misses])
                print("You have" + deathString + ".")

            '''
            However if the letter is in the word then the question mark
            is changed to that letter.
            '''
            if guess in word:
                for index in range(len(word)):
                    if guess == word[index]:
                        playersKnows = playersKnows[:int(index)] + guess + playersKnows[int(index)+1:]

        '''
        If the whole word is revealed then the player figured out
        the word.
        '''
        if '?' not in playersKnows:
            print("You have won! The word was: " + word)

        '''
        If the player got to the noose before revealing the word
        then lost.
        '''
        if misses == 8:
            print("You have lost. The word was: " + word)

        '''Ask user if the want to play again.'''
        while again != 'Yes' and again != 'No':
            again = input("Do you want to play again? (Yes/No) ")

        '''If user wants to go again a new game is called.'''
        if again == 'Yes':
            self.game(deathDictionary, wordDictionary)