'''
Author: Mark Huff
Date: 8/26/18
'''

import random

class RockPaperScissors:

    def __init__(self):
        gameDictionary = {'Rock': {'Beats': 'Scissors', 'Losses': 'Paper', 'Text': 'Rock crushes scissors.'},
                        'Paper': {'Beats': 'Rock', 'Losses': 'Scissors', 'Text': 'Paper covers rock.'},
                        'Scissors': {'Beats': 'Paper', 'Losses': 'Rock', 'Text': 'Scissors cuts paper.'}
                        }

        hands = list(gameDictionary)
        self.round(gameDictionary, hands)

    def round(self, gameDictionary, hands):
        '''
        :param gameDictionary: Stores information on each hand that can be used.
        :param hands: A list of hands that can be used.
        :return: Nothing
        '''

        print("\nWelcome to Rock, Paper, Scissors.")
        again = ''
        decision = ''

        #AI picks a hand to play against the user
        opponent = random.choice(hands)

        #User is prompted with a hand to play.
        while decision != 1 and decision != 2 and decision != 3:
            try:
                decision = int(input("Rock (1)? Paper (2)? Scissors (3)? "))
            except ValueError:
                print("Not a integer.")

        decision = hands[int(decision)-1]

        #Pulls the conditions the player can win/loss to.
        victory = gameDictionary[decision]['Beats']
        defeat = gameDictionary[decision]['Losses']

        print("You choose: " + decision)
        print("AI choose: " + opponent)

        #Determines the winner along with winners text.
        if opponent == victory:
            print(gameDictionary[decision]['Text'])
            print("You won the round")
        elif opponent == defeat:
            print(gameDictionary[opponent]['Text'])
            print("You lost the round")
        else:
            print("Its a draw.")

        # Ask user if the want to play again.
        while again != 'Yes' and again != 'No':
            again = input("Do you want to play again? (Yes/No) ")

        # If user wants to go again a new round will be called.
        if (again == 'Yes'):
            self.round(gameDictionary, hands)