import os
import random
import sys
import numpy
import re

from colorama import init
init()

from colorama import Fore, Back, Style

# Initializes a 6 x 7 matrix of zeroes
def initializeBoard():
    return numpy.zeros((6,7))

# Prints the game board
def printBoard(board):
    for row in board:
        for element in row:
            if element == 1:
                print(Fore.RED + '0  ', end=" ")
                print(Style.RESET_ALL, end=" ")
            else:
                print(int(element), "  ", end=" ")
        print ('\n')

# Randomly picks the first player
def chooseFirstPlayer():
    return "Player" if random.randrange(2) == 1 else "Computer"

# Player picks a spot to play
def playerTurn(board):
    print ('Your turn!')
    column = input('What\'s your move? ')
    if re.match('[1-7]', column):
        insertPiece(board, int(column))
    else:
        print ('Not a column')
        playerTurn(board)

# Computer chooses best place to play
def computerTurn(board, turn):
    print ('Computer is playing')


# Inserts a piece at bottom of specified column
def insertPiece(board, column):
    column -= 1
    rowCounter = 1

    for row in board:
        nextColumn = column + 1
        if rowCounter < 6 and board[rowCounter][column] == 1:
            row[column] = 1
        elif row[column] == 0 and rowCounter == 6:
            row[column] = 1

        rowCounter += 1

# Main game function
def game():
    board = initializeBoard()
    printBoard(board)
    turn = 1;

    # Pick first player and begin loop.
    # The player who played first will always
    # play first at the beginning of each round.
    firstPlayer = chooseFirstPlayer()
    while True:
        if firstPlayer == "Computer":
            print ('Computer turn')
            computerTurn(board, turn)
            turn += 1
            print ('Your turn')
            playerTurn(board)
            turn += 1

        elif firstPlayer == "Player":
            print ('Your turn')
            playerTurn(board)
            turn += 1
            print ('Computer turn')
            computerTurn(board, turn)
            turn += 1

        printBoard(board)



game()
