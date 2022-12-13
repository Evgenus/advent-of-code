from functools import cmp_to_key

from utils import list_split


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, list):
        for ai, bi in zip(a, b):
            c = compare(ai, bi)
            if c != 0:
                return c
        return compare(len(a), len(b))


def task1(filename):
    lines = read_data(filename)

    res = 0
    for i, (a, b) in enumerate(list_split(lines, ['']), 1):
        a, b = eval(a), eval(b)
        if compare(a, b) < 0:
            res += i

    return res


def task2(filename):
    lines = read_data(filename)

    d1 = [[2]]
    d2 = [[6]]

    packets = [eval(line) for line in filter(bool, lines)]
    packets += [d1, d2]
    packets.sort(key=cmp_to_key(compare))

    i1 = packets.index(d1) + 1
    i2 = packets.index(d2) + 1

    return i1 * i2


assert task1('test.txt') == 13
assert task2('test.txt') == 140
assert task1('data.txt') == 5605
assert task2('data.txt') == 24969
