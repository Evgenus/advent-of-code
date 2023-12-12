from functools import cache

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


@cache
def try_match(field, numbers, started):
    if not field:
        if not numbers:
            if started:
                return 0
            else:
                return 1
        else:
            return 0
    cell = field[0]
    if started:
        if cell in '#?':
            if not numbers:
                return 0
            new = numbers[0] - 1
            if new > 0:
                return try_match(field[1:], (new,  *numbers[1:]), True)
            else:
                return try_match(field[1:], numbers[1:], False)
        else:
            return 0
    else:
        if cell in '.?':
            return try_match(field[1:], numbers, True) + try_match(field[1:], numbers, False)
        else:
            return 0


def task1(filename):
    lines = read_data(filename)
    result = 0
    for line in lines:
        field, numbes_str = line.split()
        numbers = tuple(lmap(int, numbes_str.split(',')))
        res = try_match(field, numbers, True) + try_match(field, numbers, False)
        # print(res)
        result += res
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    for line in lines:
        field, numbes_str = line.split()
        numbers = tuple(lmap(int, numbes_str.split(',')))
        field = '?'.join([field] * 5)
        numbers *= 5
        res = try_match(field, numbers, True) + try_match(field, numbers, False)
        # print(res)
        result += res
    return result


assert task1('test.txt') == 21
assert task1('data.txt') == 8180
assert task2('test.txt') == 525152
assert task2('data.txt') == 620189727003627
