from utils import *
from collections import Counter
from itertools import pairwise
# load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def incr(line):
    for a, b in pairwise(line):
        if a >= b:
            return False
        if not 1 <= abs(a - b) <= 3:
            return False
    return True


def decr(line):
    for a, b in pairwise(line):
        if a <= b:
            return False
        if not 1 <= abs(a - b) <= 3:
            return False
    return True


def task1(filename):
    lines = read_data(filename)
    lines = lmap(str_integers, lines)
    result = sum(
        incr(line) or decr(line)
        for line in lines
    )
    print(result)
    return result


def list_pop(l, i):
    l = list(l)
    l.pop(i)
    return l


def task2(filename):
    lines = read_data(filename)
    lines = lmap(str_integers, lines)
    result = sum(
        any(
            incr(list_pop(line, i)) or decr(list_pop(line, i))
            for i in range(len(line))
        )
        for line in lines
    )
    print(result)
    return result


assert task1('test.txt') == 2
assert task1('data.txt') == 660
assert task2('test.txt') == 4
assert task2('data.txt') == 689
