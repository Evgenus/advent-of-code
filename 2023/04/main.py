from collections import defaultdict

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    lines = read_data(filename)

    result = 0
    for line in lines:
        head, pair = line.split(': ')
        win, have = pair.split(' | ')
        win = set(win.split())
        s = sum(num in win for num in have.split())
        if s:
            result += 2 ** (s - 1)
    return result


def task2(filename):
    lines = read_data(filename)

    multipliers = [1] * len(lines)
    for index, line in enumerate(lines):
        head, pair = line.split(': ')
        win, have = pair.split(' | ')
        win = set(win.split())
        s = sum(num in win for num in have.split())
        for i in range(s):
            multipliers[index + i + 1] += multipliers[index]

    return sum(multipliers)


assert task1('test.txt') == 13
assert task1('data.txt') == 24706
assert task2('test.txt') == 30
assert task2('data.txt') == 13114317
