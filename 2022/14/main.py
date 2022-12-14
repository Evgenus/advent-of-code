from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    matrix = [
        [0] * 1000 for _ in range(1000)
    ]

    def draw(x1, y1, x2, y2):
        while x1 != x2 or y1 != y2:
            matrix[x1][y1] = 1
            x1, y1 = cell_move_towards((x1, y1), (x2, y2))
        matrix[x1][y1] = 1

    maxy = 0
    lines = read_data(filename)
    for line in lines:
        numbers = str_integers(line)
        for i in range(2, len(numbers), 2):
            x1, y1 = numbers[i - 2], numbers[i - 1]
            x2, y2 = numbers[i], numbers[i + 1]

            draw(x1, y1, x2, y2)
            maxy = max(maxy, y1, y2)

    # print(maxy)
    visited = set()

    res = 0
    while True:
        x, y = 500, 0
        while True:
            ny = y + 1
            for nx in (x, x - 1, x + 1):
                if matrix[nx][ny] != 1 and (nx, ny) not in visited:
                    x, y = nx, ny
                    break
            else:
                res += 1
                visited.add((x, y))
                break
            if y > maxy:
                return res


def task2(filename):
    matrix = [
        [0] * 1000 for _ in range(1000)
    ]

    def draw(x1, y1, x2, y2):
        while x1 != x2 or y1 != y2:
            matrix[x1][y1] = 1
            x1, y1 = cell_move_towards((x1, y1), (x2, y2))
        matrix[x1][y1] = 1

    maxy = 0
    lines = read_data(filename)
    for line in lines:
        numbers = str_integers(line)
        for i in range(2, len(numbers), 2):
            x1, y1 = numbers[i - 2], numbers[i - 1]
            x2, y2 = numbers[i], numbers[i + 1]
            maxy = max(maxy, y1, y2)
            draw(x1, y1, x2, y2)

    visited = set()
    res = 0
    while (500, 0) not in visited:
        x, y = 500, 0
        while (500, 0) not in visited:
            if y == maxy + 2:
                visited.add((x, y))
                break

            ny = y + 1
            for nx in (x, x - 1, x + 1):
                if matrix[nx][ny] != 1 and (nx, ny) not in visited:
                    x, y = nx, ny
                    break
            else:
                res += 1
                visited.add((x, y))
                break
    return res


assert task1('test.txt') == 24
assert task2('test.txt') == 93
assert task1('data.txt') == 961
assert task2('data.txt') == 26375
