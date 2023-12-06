from collections import defaultdict, Counter
from functools import cache, partial

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def ways(time, distance):
    return sum(
        (time - hold) * hold > distance
        for hold in range(1, time + 1)
    )


def task1(filename):
    lines = read_data(filename)
    times = lmap(int, lines[0].split()[1:])
    distances = lmap(int, lines[1].split()[1:])

    return mul(
        ways(time, distance)
        for time, distance in zip(times, distances)
    )


def task2(filename):
    lines = read_data(filename)
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    return ways(time, distance)


assert task1('test.txt') == 288
assert task1('data.txt') == 219849
assert task2('test.txt') == 71503
assert task2('data.txt') == 29432455
