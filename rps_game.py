#!/usr/bin/env python3
from random import randint as rand
import sys

def eval_winner(p1, p2):
    """Determines the winner between two players of rock, paper, scissors

        Args: 
            p1 - the first player's choice of R, P, or S
            p2 - the second player's choice or R, P, or S

        Returns:
            1 - if player 1 wins
            2 - if player 2 / CPU wins
            0 - if the game results in a tie
    
    """
    #if player 1 chooses rock
    if p1 == "R" or p1 == "r":
        if p2 == "S":
            print('\nYou win: Rock smashes Scissors\n')
            return 1
        elif p2 == "P":
            print('\nCPU win: Paper covers Rock\n')
            return 2
        else:
            print('\nTie: Both chose Rock\n')
            return 0
    
    #player 1 chooses paper
    elif p1 == "P" or p1 == "p":
        if p2 == "R":
            print('\nYou win: Paper covers Rock\n')
            return 1
        elif p2 == "S":
            print('\nCPU win: Scissors cuts Paper\n')
            return 2
        else:
            print('\nTie: Both chose Paper\n')
            return 0

    #player 1 chooses scissors
    elif p1 == "S" or p1 == "s":
        if p2 == "P":
            print('\nYou win: Scissors cuts Paper\n')
            return 1
        elif p2 == "R":
            print('\nCPU win: Rock smashes Scissors\n')
            return 2
        else:
            print('\nTie: Both chose Scissors\n')
            return 0


def main():
    p1 = None
    p2 = None

    #when q is entered, the game will be quit
    while p1 != "q" or p1 != "Q":
        choice = ["R", "P", "S"]
        p2 = choice[rand(0,2)]
    
        #printing out menu
        print('Time to play Rock, Paper, Scissors!')
        print('\tR or r (Rock)')
        print('\tP or p (Paper)')
        print('\tS or s (Scissors)')
        print('\tQ or q (Quit)')
        p1 = input('Enter your choice: ')

        #checking if the correct input was entered 
        if len(p1) != 1:
            print('\nPlease enter a valid option\n')
        else:
            if p1.isalpha():
                if p1 == "q" or p1 == "Q":
                    break
                elif p1 == "r" or p1 == "R":
                    eval_winner(p1,p2)
                elif p1 == "p" or p1 == "P":
                    eval_winner(p1, p2)
                elif p1 == "s" or p1 == "S":
                    eval_winner(p1, p2)
                else:
                    print('\nPlease enter a valid option\n\n')
            else:
                print('\nPlease enter a valid option\n\n')



if __name__ == '__main__':
    main()
