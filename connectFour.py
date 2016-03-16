import os
import random
import sys
import numpy
import re

# Initializes a 6 x 7 matrix of zeroes
def initializeBoard():
    return numpy.zeros((6,7))

# Prints the game board
def printBoard(board):
    for row in board:
        for element in row:
            print '%i    ' % element,
        print '\n'

# Randomly picks the first player
def chooseFirstPlayer():
    return "Player" if random.randrange(2) == 1 else "Computer"

# Player picks a spot to play
def playerTurn(board):
    print 'Your turn!'
    column = input('What\'s your move? ')
    if re.match('[1-7]', column):
        insertPiece(board, int(column))
    else:
        print 'Not a valid spot'
        playerTurn(board)

# Computer chooses best place to play
def computerTurn(board, turn):
    print 'Computer is playing'


# Inserts a piece at bottom of specified column
def insertPiece(board, column):
    column -= 1
    for row in board:
        rowCounter = 1

        print 'made it here'
        if row[column + 1] == 1:
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
            print 'Computer turn'
            computerTurn(board, turn)
            turn += 1
            print 'Your turn'
            playerTurn(board)
            turn += 1

        elif firstPlayer == "Player":
            print 'Your turn'
            playerTurn(board)
            turn += 1
            print 'Computer turn'
            computerTurn(board, turn)
            turn += 1

        printBoard(board)



game()
