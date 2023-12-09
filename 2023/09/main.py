from collections import defaultdict, Counter
from functools import cache, partial

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return [
        lmap(int, line.split())
        for line in data.strip().splitlines()
    ]


def analyze(seq):
    return [
        b - a
        for a, b in zip(seq, seq[1:])
    ]


def make_history(seq):
    history = []
    while seq:
        history.append(seq)
        seq = analyze(seq)
    return history


def task1(filename):
    lines = read_data(filename)

    result = 0
    for line in lines:
        history = make_history(line)

        prev = 0
        while history:
            seq = history.pop()
            prev = seq[-1] + prev
        result += prev

    return result


def task2(filename):
    lines = read_data(filename)

    result = 0
    for line in lines:
        history = make_history(line)

        prev = 0
        while history:
            seq = history.pop()
            prev = seq[0] - prev
        result += prev

    return result


assert task1('test.txt') == 114
assert task1('data.txt') == 2008960228
assert task2('test.txt') == 2
assert task2('data.txt') == 1097
