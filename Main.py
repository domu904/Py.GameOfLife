import sys
import argparse

def main_function():
    print("Welcome to the Game of Life")
    print("Please specify size of board")
    boardSize = input()
    print("Please specify size of starting cell")
    startingCellSize = input()

    print("starting board size is " + boardSize)
    print("starting cell size is " + startingCellSize)

    board = Board(boardSize,boardSize)

main_function()
