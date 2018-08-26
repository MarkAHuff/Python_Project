'''
Author: Mark Huff
Date: 8/26/18
'''

import random

class Trivia:

    def __init__(self):
        questions = {1: {'Question': 'Who created python?', 'Answer': 'Guido van Rossum'},
                    2: {'Question': 'When was Python was first conceived?', 'Answer': '1980'},
                    3: {'Question': 'Whats the extension for a Python file?', 'Answer': '.py'},
                    4: {'Question': 'What kind of program is Python considered?', 'Answer': 'OOP'}
                    }

        self.round(questions)

    def round(self, questions):
        '''
        :param questions: A dictionary of questions and answers to them.
        :return: Nothing
        '''

        print("\nWelcome to trivia corner.")
        again = ''

        #Program randomly asks a question.
        triviaQuestion = random.randint(1, 4)

        #Prints out a random question and user answers the question.
        print(questions[triviaQuestion]['Question'], end=' ')
        userAnswer = input()

        #Checks if the user answered the question correctly.
        if userAnswer == questions[triviaQuestion]['Answer']:
            print("Correct!")
        else:
            print("Wrong!")
            print("Correct answer: " + questions[triviaQuestion]['Answer'])

        #Ask user if the want to play again.
        while again != 'No' and again != 'Yes':
            again = input("Continue trivia? (Yes/No)? ")

        #If user wants to go again a new round will be called.
        if again == 'Yes':
            self.round(questions)