'''
Author: Mark Huff
Date: 8/26/18
'''

import random

class HighLow:

    def __init__(self):
        diceOne = 0
        diceTwo = 0
        diceValue = 0
        self.round(diceOne, diceTwo, diceValue)

    def round(self, diceOne, diceTwo, diceValue):
        '''
        :param diceOne: The roll of the first dice.
        :param diceTwo: The roll of the second dice.
        :param diceValue: The value of the combined rolls.
        :return: Nothing
        '''

        print("\nDecide if the two dice rolled combined is either higher, lower, equal to seven.")
        again = ''
        prediction = ''

        print("What do you decide for this roll?")
        print("1. Higher dice value then 7.")
        print("2. Lower dice value then 7.")
        print("3. Equal dice value of 7.")

        #Input of the user prediction.
        while prediction != 1 and prediction != 2 and prediction != 3:
            try:
                prediction = int(input("What you think is the dice value will be? "))
            except ValueError:
                print("Not a integer.")

        #Roll both of the dice.
        diceOne = random.randint(1, 6)
        diceTwo = random.randint(1, 6)

        #Value of rolls.
        diceValue = int(diceOne) + int(diceTwo)

        #Result of the roll compared to prediction.
        print("The two dice rolled add up to: " + str(diceValue))
        if diceValue > 7:
            if prediction == 1:
                print("You predicted the roll!")
            else:
                print("You didn't predict the roll.")
        elif diceValue < 7:
            if prediction == 2:
                print("You predicted the roll!")
            else:
                print("You didn't predict the roll.")
        else:
            if prediction == 3:
                print("You predicted the roll!")
            else:
                print("You didn't predict the roll.")

        #Ask user if the want to play again.
        while again != 'Yes' and again != 'No':
            again = input("Do you want to play again? (Yes/No) ")

        #If user wants to go again a new round will be called.
        if again == 'Yes':
            self.round(diceOne, diceTwo, diceValue)