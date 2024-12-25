from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    result = 0

    combs = list_split(lines, [''])
    locks = []
    keys = []

    for comb in combs:
        if comb[0] == '#' * len(comb[0]):
            locks.append([
                pin.count('#') - 1
                for pin in (zip(*comb))
            ])
        else:
            keys.append([
                pin.count('#') - 1
                for pin in (zip(*comb))
            ])

    for key in keys:
        for lock in locks:
            if all(a + b <= 5 for a, b in zip(key, lock)):
                result += 1

    print(f"1: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 3
assert task1('data.txt') == 3690
