from functools import cmp_to_key

from utils import list_split


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        else:
            return a < b
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, list):
        for ai, bi in zip(a, b):
            c = compare(ai, bi)
            if c is not None:
                return c
        if len(a) < len(b):
            return True
        if len(a) > len(b):
            return False
        return None


def task1(filename):
    lines = read_data(filename)

    res = 0
    for i, (a, b) in enumerate(list_split(lines, ['']), 1):
        a, b = eval(a), eval(b)
        if compare(a, b):
            res += i

    return res


def cmp(a, b):
    if compare(a, b) is True:
        return -1
    if compare(a, b) is False:
        return 1
    return 0


def test2(filename):
    lines = read_data(filename)
    d1 = [[2]]
    d2 = [[6]]

    packets = [
        eval(line)
        for line in filter(bool, lines)
    ] + [d1, d2]

    packets.sort(key=cmp_to_key(cmp))

    i1 = packets.index(d1) + 1
    i2 = packets.index(d2) + 1

    return i1 * i2


assert task1('test.txt') == 13
assert test2('test.txt') == 140
assert task1('data.txt') == 5605
assert test2('data.txt') == 24969
