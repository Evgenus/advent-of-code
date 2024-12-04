from utils import *
from collections import Counter
# load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def task1(filename):
    lines = read_data(filename)
    pairs = [lmap(int, line.split()) for line in lines]
    first, second = zip(*pairs)
    first = sorted(first)
    second = sorted(second)
    result = sum(abs(a - b) for a, b in zip(first, second))
    return result


def task2(filename):
    lines = read_data(filename)
    pairs = [lmap(int, line.split()) for line in lines]
    first, second = zip(*pairs)
    first = sorted(first)
    second = Counter(second)
    result = sum(a * second[a] for a in first)
    print(result)
    return result


assert task1('test.txt') == 11
assert task1('data.txt') == 1223326
assert task2('test.txt') == 31
assert task2('data.txt') == 21070419
