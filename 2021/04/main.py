from functools import partial

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    numbers, *boards = list_split(data.strip().splitlines(), [''])

    numbers = lmap(int, numbers[0].split(','))
    boards = [
        [
            lmap(int, line.split())
            for line in board
        ]
        for board in boards
    ]

    return numbers, boards


class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.board = {}
        self.sum = 0
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                self.board[value] = (i, j)
                self.sum += value
        self.rows = lmap(set, matrix)
        self.cols = lmap(set, zip(*matrix))

    def call(self, value):
        if value not in self.board:
            return False
        i, j = self.board[value]
        self.matrix[i][j] = ' '
        self.rows[i].remove(value)
        self.cols[j].remove(value)
        del self.board[value]
        self.sum -= value
        return not self.rows[i] or not self.cols[j]


def task1(filename):
    numbers, boards = read_data(filename)
    boards = lmap(Board, boards)
    for number in numbers:
        for board in boards:
            if board.call(number):
                return board.sum * number


def task2(filename):
    numbers, boards = read_data(filename)
    boards = lmap(Board, boards)
    for number in numbers:
        if len(boards) == 1:
            board = boards[0]
            if board.call(number):
                return board.sum * number
        else:
            boards = [
                board
                for board in boards
                if not board.call(number)
            ]


assert task1('test.txt') == 4512
assert task1('data.txt') == 33462
assert task2('test.txt') == 1924
assert task2('data.txt') == 30070
