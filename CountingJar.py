'''
Author: Mark Huff
Date: 8/26/18
'''

import random


class CountingJar:

    def __init__(self):
        hintDictionary = {(1000, 800): 'The jar is pretty close to full.',
                            (799, 650): 'Looks like the jar is around 3/4 full.',
                            (649, 500): 'Looks like the jar is little over half full.',
                            (499, 250): 'Looks like the jar is around 1/4 full.',
                            (249, 1): 'Looks like the jar has some contents in it.'
                        }

        self.prediction(hintDictionary)

    def prediction(self, hintDictionary):
        '''
        :param hintDictionary: Stores information on how full the jar is.
        :return: Nothing
        '''

        print("\nWelcome to the counting jar game. You guess how much items are in the jar."
                " Hint: The max amount of items in the jar is a 1,000.")
        again = ''

        #'Places' a random amount of items in the jar.
        amountInJar = random.randint(1, 1000)

        #Prints out the hint that matches the amount in the jar.
        for tupleRange in hintDictionary:
            if amountInJar <= tupleRange[0] and amountInJar > tupleRange[1]:
                print(hintDictionary[tupleRange])
                break;

        #Asks for the user's guess.
        while True:
            try:
                guess = int(input("How much contents are in the jar? "))
                break
            except ValueError:
                print("Not a integer.")

        #Checks the amount in jar to the user's guess.
        if guess > amountInJar:
            print("Your guess is higher than what is in the jar.")
        elif guess < amountInJar:
            print("Your guess is lower than the jars contents.")
            print("Amount in the jar: " + str(amountInJar))
            print("You are " + str(int(amountInJar)-int(guess)) + " away from the amount in the jar.")
        else:
            print("You picked the exact amount in the jar.")

        # Ask user if the want to play again.
        while again != 'Yes' and again != 'No':
            again = input("Do you want to play again? (Yes/No) ")

        # If user wants to go again a new jar will be generated.
        if (again == 'Yes'):
            self.prediction(hintDictionary)


'''
1000-800
799-650
649-500
499-250
250-0
'''