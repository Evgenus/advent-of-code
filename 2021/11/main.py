from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return [
        lmap(int, line)
        for line in data.strip().splitlines()
    ]


def run_step(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            matrix[i][j] += 1

    flushed = set()
    while True:
        flushes = {
            (i, j)
            for i in range(n)
            for j in range(m)
            if matrix[i][j] > 9 and (i, j) not in flushed
        }
        if not flushes:
            break
        for i, j in flushes:
            for di, dj in matrix_next8(matrix, i, j):
                matrix[di][dj] += 1
        flushed |= flushes
    for i, j in flushed:
        matrix[i][j] = 0
    return flushed


def task1(filename):
    matrix = read_data(filename)
    score = 0
    for step in range(100):
        score += len(run_step(matrix))
    return score


def task2(filename):
    matrix = read_data(filename)
    n = len(matrix)
    m = len(matrix[0])

    step = 0
    while True:
        step += 1
        if len(run_step(matrix)) == m * n:
            return step


assert task1('test.txt') == 1656
assert task1('data.txt') == 1713
assert task2('test.txt') == 195
assert task2('data.txt') == 502
