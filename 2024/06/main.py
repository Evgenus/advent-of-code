from utils import *
from collections import Counter
from itertools import pairwise
load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)

    n = len(lines)
    m = len(lines[0])

    pos = 0, 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                pos = i, j

    vel = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    dir = 0
    places = set()
    while True:
        places.add(pos)
        next = pos[0] + vel[dir][0], pos[1] + vel[dir][1]
        if not (0 <= next[0] < n and 0 <= next[1] < m):
            break
        if lines[next[0]][next[1]] == '#':
            dir = (dir + 1) % 4
        else:
            pos = next

    result = len(places)

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    lines = lmap(list, lines)
    result = 0

    n = len(lines)
    m = len(lines[0])

    vel = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    def stuck(pos):
        dir = 0
        places = defaultdict(set)
        while True:
            if dir in places[pos]:
                return True
            places[pos].add(dir)
            next = pos[0] + vel[dir][0], pos[1] + vel[dir][1]
            if not (0 <= next[0] < n and 0 <= next[1] < m):
                break
            if lines[next[0]][next[1]] == '#':
                dir = (dir + 1) % 4
            else:
                pos = next
        return False

    pos = 0, 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                pos = i, j

    for i, line in enumerate(lines):
        print(i)
        for j, c in enumerate(line):
            if lines[i][j] == '#':
                continue
            lines[i][j] = '#'
            if stuck(pos):
                result += 1
            lines[i][j] = '.'

    print(f"2: {filename}, {result}")
    return result


assert task1('test.txt') == 41
assert task1('data.txt') == 5239
assert task2('test.txt') == 6
assert task2('data.txt') == 0
