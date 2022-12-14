from utils import *


def draw(matrix, x1, y1, x2, y2):
    while x1 != x2 or y1 != y2:
        matrix[x1][y1] = 1
        x1, y1 = cell_move_towards((x1, y1), (x2, y2))

    matrix[x1][y1] = 1


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    matrix = [
        [0] * 1000 for _ in range(1000)
    ]

    maxy = 0
    for line in lines:
        pairs = str_integers(line)
        for i in range(2, len(pairs), 2):
            x1, y1 = pairs[i - 2], pairs[i - 1]
            x2, y2 = pairs[i], pairs[i + 1]

            draw(matrix, y1, x1, y2, x2)
            maxy = max(maxy, y1, y2)

    return matrix, maxy


def print_result(matrix, visited):
    for x, y in visited:
        matrix[y][x] = '2'

    boundaries = matrix_boundaries(matrix, lambda cell: cell != 0)
    matrix_print(matrix_crop(matrix, *boundaries), translation={'0': '.', '1': '#', '2': 'o'})


def fall_one_step(matrix, visited, x, y):
    for nx in (x, x - 1, x + 1):
        if matrix[y + 1][nx] != 1 and (nx, y + 1) not in visited:
            return nx, y + 1
    return x, y


def task1(filename):
    matrix, maxy = read_data(filename)

    start = 500, 0
    visited = set()
    res = 0
    while True:
        x, y = start
        while True:
            nx, ny = fall_one_step(matrix, visited, x, y)
            if (nx, ny) == (x, y):
                break
            x, y = nx, ny
            if y > maxy:
                # print_result(matrix, visited)
                return res
        res += 1
        visited.add((x, y))


def task2(filename):
    matrix, maxy = read_data(filename)

    start = 500, 0
    visited = set()
    res = 0
    while True:
        x, y = start
        while True:
            nx, ny = fall_one_step(matrix, visited, x, y)
            if (nx, ny) == (x, y):
                break
            x, y = nx, ny
            if y > maxy:
                break
        res += 1
        visited.add((x, y))
        if (x, y) == start:
            break

    # print_result(matrix, visited)
    return res


assert task1('test.txt') == 24
assert task2('test.txt') == 93
assert task1('data.txt') == 961
assert task2('data.txt') == 26375
