from functools import partial

from utils import (
    chain,
    list_split,
)


def read_data():
    with open('data.txt', 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    groups = list_split(lines, [''])
    return map(chain(partial(map, int), sum), groups)


def task1():
    groups = read_data()
    return max(groups)


def task2():
    groups = read_data()
    return sum(sorted(groups)[-3:])


print(task1())
print(task2())
