from utils import (
    cell_dist8,
    cell_move_towards,
)

MOVES = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


def move(pos, dir):
    dx, dy = MOVES[dir]
    return pos[0] + dx, pos[1] + dy


def task(filename, length):
    with open(filename, 'r') as f:
        data = f.read()

    head = (0, 0)
    rope = [head] * length
    positions = set()

    for line in data.strip().splitlines():
        dir, amount = line.split()
        amount = int(amount)
        for _ in range(0, amount):
            rope[0] = move(rope[0], dir)
            for i in range(1, len(rope)):
                if cell_dist8(rope[i], rope[i - 1]) > 1:
                    rope[i] = cell_move_towards(rope[i], rope[i - 1])
            positions.add(rope[-1])

    return len(positions)


assert task('test.txt', 2) == 13
assert task('data.txt', 2) == 6266
assert task('test2.txt', 10) == 36
assert task('data.txt', 10) == 2369
