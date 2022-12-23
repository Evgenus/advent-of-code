from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(int, data.strip().splitlines())


def task1(filename):
    numbers = read_data(filename)
    return sum(
        numbers[i - 1] < numbers[i]
        for i in range(1, len(numbers))
    )


def task2(filename):
    numbers = read_data(filename)
    windows = lmap(sum, iter_window(numbers, 3))
    return sum(
        windows[i - 1] < windows[i]
        for i in range(1, len(windows))
    )


assert task1('test.txt') == 7
assert task1('data.txt') == 1292
assert task2('test.txt') == 5
assert task2('data.txt') == 1262
