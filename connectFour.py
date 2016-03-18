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

def printScreen(board):
    printGameTitle()
    printBoard(board)

def printGameTitle():
    os.system("clear")
    print(" _____                             _       ___")
    print("/  __ \                           | |     /   |")
    print("| /  \/ ___  _ __  _ __   ___  ___| |_   / /| |")
    print("| |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |")
    print("| \__/\ (_) | | | | | | |  __/ (__| |_  \___  |")
    print(" \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/")
    print(" ")


# Prints the game board
def printBoard(board):
    for row in board:
        print("         -----------------------------")
        print("         |", end="")
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
    print("         -----------------------------")
    print("         | |                       | |")
    print("         | |                       | |")
    print("         | |                       | |")
    print("        /___\\                     /___\\")
    print(" ")

# Randomly picks the first and second player
def chooseFirstPlayer():
    return ("Player", "Computer") if random.randrange(2) == 1 else ("Computer", "Player")

# Player picks a spot to play
def playerTurn(board):
    playerFlag = 1

    while True:
        column = input('What\'s your move? ')
        if re.match('[1-7]', column) :
            column = int(column)

            if board[0][column - 1] == 1 or board[0][column - 1] == -1: 
                print("That column is full")
                continue

            insertPiece(board, column, playerFlag)
            break

        else:
            print ('Not a column')

# Computer chooses best place to play
def computerTurn(board, turn):
    computerFlag = -1
    print ('Choosing move...')
    time.sleep(0) #Set "thinking" time to 0 while we're testing

    column = random.randrange(8)
    while board[0][column - 1] == 1 or board[0][column - 1] == -1:
        column = random.randrange(8)

    insertPiece(board, column, computerFlag)

# Inserts a piece at bottom of specified column
def insertPiece(board, column, flag):
    column -= 1
    nextRowsIndex = 1 #Used to track the row under the current row

    #  
    for row in board:
        if nextRowsIndex< 6 and (board[nextRowsIndex][column] == 1 or board[nextRowsIndex][column] == -1):
            row[column] = flag
            break
        elif nextRowsIndex == 6 and row[column] == 0: # Special case for when on the bottom row
            row[column] = flag
            break

        nextRowsIndex += 1

# Checks if there is a tie
def gameIsTie(board):
    printScreen(board)
    print("Draw!")

# Main game function
def game():

    init() #colorama required init function
    board = initializeBoard()
    turn = 1

    # Pick first player and begin loop.
    # The player who played first will always
    # play first at the beginning of each round.
    firstPlayer, secondPlayer = chooseFirstPlayer()
    while True:

        printScreen(board)
        print(firstPlayer + "'s turn")

        if firstPlayer == "Computer":
            computerTurn(board, turn)
        else:
            playerTurn(board)
        turn += 1

        printScreen(board)
        print(secondPlayer + "'s turn")

        if firstPlayer == "Computer":
            playerTurn(board)
        else:
            computerTurn(board, turn)
        turn += 1
        
        if turn == 43:
            gameIsTie(board)
            break

# Start of the game
game()
