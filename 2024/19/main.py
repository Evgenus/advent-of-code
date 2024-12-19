from utils import *
from collections import Counter
from itertools import pairwise
from functools import cache

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    result = 0

    towels, designs = list_split(lines, [''])
    towels = towels[0].split(', ')

    @cache
    def possible(design):
        if not design:
            return True
        for towel in towels:
            if design.startswith(towel) and possible(design[len(towel):]):
                return True
        return False

    for design in designs:
        if possible(design):
            result += 1

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    towels, designs = list_split(lines, [''])
    towels = towels[0].split(', ')

    @cache
    def possible(design):
        if not design:
            return 1
        w = 0
        for towel in towels:
            if design.startswith(towel):
                w += possible(design[len(towel):])
        return w

    for design in designs:
        result += possible(design)

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 6
assert task1('data.txt') == 206
assert task2('test.txt') == 16
assert task2('data.txt') == 622121814629343
