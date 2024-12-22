from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def calc(secret):
    secret = secret ^ (secret * 64)
    secret = secret % 16777216
    secret = secret ^ (secret // 32)
    secret = secret % 16777216
    secret = secret ^ (secret * 2048)
    secret = secret % 16777216
    return secret


def task1(filename):
    lines = read_data(filename)
    result = 0

    for line in lines:
        secret = int(line)
        for i in range(2000):
            secret = calc(secret)
        result += secret


    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    best = Counter()
    for line in lines:
        changes = {}
        change = []
        secret = int(line)
        prev = secret % 10
        for i in range(2000):
            secret = calc(secret)
            last = secret % 10
            change.append(last - prev)
            if len(change) >= 4:
                change = change[-4:]
                c = tuple(change)
                if c not in changes:
                    changes[c] = last
            prev = last
        for change, value in changes.items():
            best[change] += value
    result = best.most_common(1)[0][1]

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test1.txt') == 37327623
assert task1('data.txt') == 14082561342
assert task2('test2.txt') == 23
assert task2('data.txt') == 1568
