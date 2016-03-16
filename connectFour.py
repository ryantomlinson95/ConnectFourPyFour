import os
import sys
import numpy


def initializeBoard():
    return numpy.zeros(shape=(6,7)).astype('int')

def printBoard(board):
    for row in board:
        for element in row:
            print '%i    ' % element,
        print '\n'

def game():
    board = initializeBoard()
    printBoard(board)

game()
