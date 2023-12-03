from collections import defaultdict

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def is_symbol(c: str):
    return not c.isdigit() and c != "." and c != ""


def check(field, i, j, func):
    if func(field[i - 1, j - 1]):
        return True
    if func(field[i - 1, j]):
        return True
    if func(field[i - 1, j + 1]):
        return True

    if func(field[i, j - 1]):
        return True
    if func(field[i, j + 1]):
        return True

    if func(field[i + 1, j - 1]):
        return True
    if func(field[i + 1, j]):
        return True
    if func(field[i + 1, j + 1]):
        return True

    return False


def task1(filename):
    lines = read_data(filename)
    field = defaultdict(str)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            field[i, j] = char

    numbers = []
    for i, line in enumerate(lines):
        buf = []
        ok = False
        for j, char in enumerate(line):
            if char.isdigit():
                ok |= check(field, i, j, is_symbol)
                buf.append(char)
            else:
                if buf and ok:
                    numbers.append(''.join(buf))
                buf = []
                ok = False

        if buf and ok:
            numbers.append(''.join(buf))

    return sum(map(int, numbers))


def task2(filename):
    lines = read_data(filename)
    field = defaultdict(str)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            field[i, j] = char

    numbers = []
    places = defaultdict(lambda: -1)
    for i, line in enumerate(lines):
        buf = []
        coords = []
        ok = False
        for j, char in enumerate(line):
            if char.isdigit():
                ok |= check(field, i, j, is_symbol)
                buf.append(char)
                coords.append((i, j))
            else:
                if buf and ok:
                    for coord in coords:
                        places[coord] = len(numbers)
                    numbers.append(''.join(buf))
                buf = []
                coords = []
                ok = False

        if buf and ok:
            for coord in coords:
                places[coord] = len(numbers)
            numbers.append(''.join(buf))

    result = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            indexes = set()

            def aggr(index):
                if index >= 0:
                    indexes.add(index)
                return False

            if char == "*":
                check(places, i, j, aggr)
                if len(indexes) == 2:
                    prod = 1
                    for index in indexes:
                        prod *= int(numbers[index])
                    result += prod

    return result


assert task1('test.txt') == 4361
assert task1('data.txt') == 553079
assert task2('test.txt') == 467835
assert task2('data.txt') == 84363105
