import re
from itertools import zip_longest

from utils import list_split


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    data1, data2 = list_split(data.splitlines(), [''])

    rows = zip_longest(
        *[line[1::4]
            for line in data1[:-1][::-1]
        ],
        fillvalue=' '
    )

    rows = [[]] + [
        [
            box
            for box in row
            if box != ' '
        ]
        for row in rows
    ]

    moves = []
    for line in data2:
        move = re.findall(r'(\d+) from (\d+) to (\d+)', line)
        amount, src, dst = move[0]
        moves.append((int(amount), int(src), int(dst)))

    return rows, moves


def task(filename, reverse):
    rows, moves = read_data(filename)
    for amount, src, dst in moves:
        stack = rows[src][-amount:]
        if reverse:
            stack = stack[::-1]
        rows[dst].extend(stack)
        rows[src][-amount:] = []

    top = [row[-1] for row in rows[1:]]
    return ''.join(top)


assert task('test.txt', True) == "CMZ"
assert task('test.txt', False) == "MCD"
assert task('data.txt', True) == "TDCHVHJTG"
assert task('data.txt', False) == "NGCMPJLHV"
