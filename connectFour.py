import os
import time
import random
import numpy
import re
from colorama import init
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
    return ("Player", "Computer") if random.randrange(2) == 1 else ("Computer", "Player")

# Player picks a spot to play
def playerTurn(board, playerFlag):
    while True:
        column = input('What\'s your move? ')
        if re.match('[1-7]', column):
            insertPiece(board, int(column), playerFlag)
            break
        else:
            print ('Not a column')

# Computer chooses best place to play
def computerTurn(board, turn, computerFlag):
    print ('Choosing move...')
    time.sleep(1.5)
    column = random.randrange(8)
    while board[0][int(column) - 1] == 1 or board[0][int(column) - 1] == -1:
        column = random.randrange(8)

    insertPiece(board, int(column), computerFlag)

# Inserts a piece at bottom of specified column
def insertPiece(board, column, flag):
    column -= 1
    rowCounter = 1

    for row in board:
        if rowCounter < 6 and (board[rowCounter][column] == 1 or board[rowCounter][column] == -1):
            row[column] = flag
            break
        elif row[column] == 0 and rowCounter == 6:
            row[column] = flag
            break

        rowCounter += 1

# Main game function
def game():

    init() #colorama required init function
    board = initializeBoard()
    turn = 1
    playerFlag = 1
    computerFlag = -1

    # Pick first player and begin loop.
    # The player who played first will always
    # play first at the beginning of each round.
    firstPlayer, secondPlayer = chooseFirstPlayer()
    while True:
        
        os.system("clear")
        print(firstPlayer + "'s turn")
        printBoard(board)

        if firstPlayer == "Computer":
            computerTurn(board, turn, computerFlag)
        else:
            playerTurn(board, playerFlag)

        turn += 1

        os.system("clear")
        print(secondPlayer + "'s turn")
        printBoard(board)

        if firstPlayer == "Computer":
            playerTurn(board, playerFlag)
        else:
            computerTurn(board, turn, computerFlag)

        turn += 1

# Start of the game
game()
