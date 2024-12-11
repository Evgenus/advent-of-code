from utils import *
from collections import Counter
from itertools import pairwise
from functools import cache

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

@cache
def calc(number, k):
    if k == 0:
        return 1
    if number == 0:
        return calc(1, k - 1)
    s = str(number)
    if len(s) % 2 == 0:
        s1 = int(s[:len(s) // 2])
        s2 = int(s[len(s) // 2:])
        return calc(s1, k - 1) + calc(s2, k - 1)
    return calc(number * 2024, k - 1)


def task1(filename):
    lines = read_data(filename)
    result = 0
    stones = str_integers(lines[0])

    for stone in stones:
        result += calc(stone, 25)

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    stones = str_integers(lines[0])

    for stone in stones:
        result += calc(stone, 75)

    print(f"2: {filename}, {result}")
    return result


load_input()
assert task1('test.txt') == 55312
assert task1('data.txt') == 189547
assert task2('data.txt') == 224577979481346
