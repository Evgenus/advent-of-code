from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    sdots, sfolds = list_split(data.strip().splitlines(), [''])
    dots = set()
    for line in sdots:
        x, y = line.split(',')
        dots.add((int(x), int(y)))
    folds = []
    for line in sfolds:
        axis, pos = line.rsplit(' ', 1)[-1].split('=')
        pos = int(pos)
        folds.append((axis, pos))
    return dots, folds


def task(filename, full=True):
    dots, folds = read_data(filename)
    if not full:
        folds = folds[:1]

    maxx = max(x for x, y in dots)
    maxy = max(y for x, y in dots)

    for axis, pos in folds:
        if axis == 'x':
            dots = {
                (x, y) if x < pos else (pos * 2 - x, y)
                for x, y in dots
            }
            maxx = pos - 1
        else:
            dots = {
                (x, y) if y < pos else (x, pos * 2 - y)
                for x, y in dots
            }
            maxy = pos - 1

    if full:
        matrix = [['.'] * (maxx + 1) for _ in range(maxy + 1)]
        for x, y in dots:
            matrix[y][x] = '#'
        matrix_print(matrix)

    return len(dots)


assert task('test.txt', False) == 17
assert task('data.txt', False) == 735
task('data.txt')
