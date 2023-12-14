from itertools import count

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(list, data.strip().splitlines())


def task1(filename):
    matrix = read_data(filename)

    n = len(matrix)
    m = len(matrix[0])

    for j in range(m):
        while True:
            moved = False
            for i in range(n - 1):
                if matrix[i][j] == '.' and matrix[i + 1][j] == 'O':
                    matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                    moved = True
            if not moved:
                break

    result = 0
    for j in range(m):
        for i in range(n):
            if matrix[i][j] == 'O':
                result += n - i
    return result


def task2(filename):
    matrix = read_data(filename)

    n = len(matrix)
    m = len(matrix[0])

    cache = {}
    results = {}
    for cycle in count(1):
        # W
        for j in range(m):
            while True:
                moved = False
                for i in range(n - 1):
                    if matrix[i][j] == '.' and matrix[i + 1][j] == 'O':
                        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                        moved = True
                if not moved:
                    break

        # W
        for i in range(n):
            while True:
                moved = False
                for j in range(m - 1):
                    if matrix[i][j] == '.' and matrix[i][j + 1] == 'O':
                        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
                        moved = True
                if not moved:
                    break

        # S
        for j in range(m):
            while True:
                moved = False
                for i in range(n - 1, 0, -1):
                    if matrix[i][j] == '.' and matrix[i - 1][j] == 'O':
                        matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
                        moved = True
                if not moved:
                    break

        # E
        for i in range(n):
            while True:
                moved = False
                for j in range(m - 1, 0, -1):
                    if matrix[i][j] == '.' and matrix[i][j - 1] == 'O':
                        matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
                        moved = True
                if not moved:
                    break

        key = '\n'.join(lmap(''.join, matrix))
        if key in cache:
            prev = cache[key]
            return results[prev + (1000000000 - prev) % (cycle - prev)]
        cache[key] = cycle

        result = 0
        for j in range(m):
            for i in range(n):
                if matrix[i][j] == 'O':
                    result += n - i
        results[cycle] = result


assert task1('test.txt') == 136
assert task1('data.txt') == 109665
assert task2('test.txt') == 64
assert task2('data.txt') == 96061
