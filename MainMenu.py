'''
Author: Mark Huff
Date: 8/26/18
'''

from HighLow import HighLow
from RockPaperScissors import RockPaperScissors
from CountingJar import CountingJar
from Hangman import Hangman
from Trivia import Trivia

def main():
    choice = 0

    while choice != 6:
        '''Main menu screen.'''
        print("\nWelcome to the Python Fair.")
        print("1. Higher or lower?")
        print("2. Rock, Paper, Scissors")
        print("3. Counting jar")
        print("4. Hangman")
        print("5. Trivia")
        print("6. Leave")

        '''User input on the main menu.'''
        while True:
            try:
                choice = int(input("What do you want to do? "))
                break
            except ValueError:
                print("Not proper input.")

        '''Navigation to a selected game.'''
        if choice == 1:
            HighLow()
        elif choice == 2:
            RockPaperScissors()
        elif choice == 3:
            CountingJar()
        elif choice == 4:
            Hangman()
        elif choice == 5:
            Trivia()
        elif choice == 6:
            print("Goodbye.")
        else:
            print("Not a option.")

if __name__=="__main__":
    main()