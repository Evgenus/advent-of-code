from collections import defaultdict, Counter
from functools import cache, partial

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def hash(step):
    curr = 0
    for char in step:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr


def task1(filename):
    lines = read_data(filename)
    steps = lines[0].split(',')
    return sum(map(hash, steps))


def task2(filename):
    lines = read_data(filename)
    steps = lines[0].split(',')
    boxes = defaultdict(dict)
    for step in steps:
        if '=' in step:
            lens, num = step.split('=')
            boxes[hash(lens)][lens] = int(num)
        else:
            lens = step[:-1]
            boxes[hash(lens)].pop(lens, None)
    return sum(
        (box + 1) * index * value
        for box, lenses in boxes.items()
        for index, value in enumerate(lenses.values(), start=1)
    )


assert task1('test.txt') == 1320
assert task1('data.txt') == 503154
assert task2('test.txt') == 145
assert task2('data.txt') == 251353
