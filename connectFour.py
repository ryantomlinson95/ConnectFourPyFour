import os
import time
import random
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
        print("-----------------------------")
        print("|", end="")
        for element in row:
            if element == 1:
                print(Fore.RED + ' 0 ', end="")
                print(Style.RESET_ALL, end="")
                print('|', end="")
            elif element == -1:
                print(Fore.YELLOW + ' 0 ', end="")
                print(Style.RESET_ALL, end="")
                print('|', end="")
            else:
                print("   |", end="")
        print ('')
    print("-----------------------------")

#comment

# Randomly picks the first player
def chooseFirstPlayer():
    return "Player" if random.randrange(2) == 1 else "Computer"

# Player picks a spot to play
def playerTurn(board):
    column = input('What\'s your move? ')
    if re.match('[1-7]', column):
        insertPlayerPiece(board, int(column))
    else:
        print ('Not a column')
        playerTurn(board)

# Computer chooses best place to play
def computerTurn(board, turn):
    print ('Choosing move...')
    time.sleep(2)
    column = random.randrange(8)
    while board[0][int(column) - 1] == 1 or board[0][int(column) - 1] == -1:
        column = random.randrange(8)

    insertComputerPiece(board, int(column))

# Inserts a piece at bottom of specified column
def insertComputerPiece(board, column):
    column -= 1
    rowCounter = 1

    for row in board:
        nextColumn = column + 1
        if rowCounter < 6 and (board[rowCounter][column] == 1 or board[rowCounter][column] == -1):
            row[column] = -1
            break
        elif row[column] == 0 and rowCounter == 6:
            row[column] = -1
            break

        rowCounter += 1

# Inserts a piece at bottom of specified column
def insertPlayerPiece(board, column):
    column -= 1
    rowCounter = 1

    for row in board:
        nextColumn = column + 1
        if rowCounter < 6 and (board[rowCounter][column] == 1 or board[rowCounter][column] == -1):
            row[column] = 1
            break
        elif row[column] == 0 and rowCounter == 6:
            row[column] = 1
            break

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
            os.system('clear')
            print ('Computer turn')
            printBoard(board)
            computerTurn(board, turn)
            turn += 1
            os.system('clear')
            print ('Your turn')
            printBoard(board)
            playerTurn(board)
            turn += 1

        elif firstPlayer == "Player":
            os.system('clear')
            print ('Your turn')
            printBoard(board)
            playerTurn(board)
            turn += 1
            os.system('clear')
            print ('Computer turn')
            printBoard(board)
            computerTurn(board, turn)
            turn += 1




game()
