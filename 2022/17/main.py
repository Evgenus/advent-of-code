from collections import defaultdict

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip()


SHAPE1 = [
    [1, 1, 1, 1]
]

SHAPE2 = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
]

SHAPE3 = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 1, 1],
]

SHAPE4 = [
    [1],
    [1],
    [1],
    [1],
]

SHAPE5 = [
    [1, 1],
    [1, 1],
]

SHAPES = [
    SHAPE1,
    SHAPE2,
    SHAPE3,
    SHAPE4,
    SHAPE5,
]


def intersects(matrix, shape, x, y):
    for sy in range(len(shape)):
        for sx in range(len(shape[sy])):
            if shape[sy][sx] == 1 and matrix[y + sy][x + sx] == 1:
                return True
    return False


def add_rows(matrix, rows, width):
    for _ in range(rows):
        matrix.appendleft([0] * width)


def trim(matrix):
    while all(cell == 0 for cell in matrix[0]):
        matrix.popleft()


def plot(matrix, shape, x, y):
    for sy in range(len(shape)):
        for sx in range(len(shape[sy])):
            if shape[sy][sx] == 1:
                matrix[y + sy][x + sx] = 1


WIDTH = 7


def task(filename, rocks_count):
    moves = read_data(filename)

    matrix = deque()
    matrix.append([1] * WIDTH)

    rocks = 0
    s = 0
    move = 0
    seen = defaultdict(list)
    while rocks < min(rocks_count, 10000):
        shape = SHAPES[s]
        add_rows(matrix, 3 + len(shape), WIDTH)
        x = 2
        y = 0
        while True:
            if moves[move] == '>':
                if x + len(shape[0]) < WIDTH:
                    if not intersects(matrix, shape, x + 1, y):
                        x += 1
            else:
                if x > 0:
                    if not intersects(matrix, shape, x - 1, y):
                        x -= 1
            move = (move + 1) % len(moves)
            if intersects(matrix, shape, x, y + 1):
                break
            y += 1
        plot(matrix, shape, x, y)
        rocks += 1
        s = (s + 1) % len(SHAPES)
        trim(matrix)

        # print('=' * 80)
        # matrix_print(matrix, translation={0: '.', 1: '#'})

        if len(matrix) > 20:
            matrix_top = tuple(int(''.join(map(str, matrix[i])), 2) for i in range(20))
            key = (matrix_top, move, s)
            seen[key].append((rocks, len(matrix) - 1))
            if len(seen[key]) > 1:
                r1, h1 = seen[key][-2]
                r2, h2 = seen[key][-1]
                if (rocks_count - r1) % (r2 - r1) == 0:
                    result = (rocks_count - r1) // (r2 - r1) * (h2 - h1) + h1
                    print(f'{filename=} {rocks_count=}')
                    print(f'after {r1} rocks height is {h1}')
                    print(f'after {r2} rocks height is {h2}')
                    print(f'({rocks_count} - {r1}) // ({r2} - {r1}) * ({h2} - {h1}) + {h1} == {result}')
                    return result

    return len(matrix) - 1


assert task('test.txt', 2022) == 3068
assert task('data.txt', 2022) == 3151
assert task('test.txt', 1000000000000) == 1514285714288
assert task('data.txt', 1000000000000) == 1560919540245
