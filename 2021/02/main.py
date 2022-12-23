from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return [
        (cmd, int(value))
        for cmd, value in map(str.split, data.strip().splitlines())
    ]


def task1(filename):
    depth = 0
    x = 0
    commands = read_data(filename)
    for cmd, value in commands:
        if cmd == 'forward':
            x += value
        elif cmd == 'up':
            depth -= value
            depth = max(depth, 0)
        elif cmd == 'down':
            depth += value
    return x * depth


def task2(filename):
    depth = 0
    aim = 0
    x = 0
    commands = read_data(filename)
    for cmd, value in commands:
        if cmd == 'forward':
            x += value
            depth += aim * value
        elif cmd == 'up':
            aim -= value
        elif cmd == 'down':
            aim += value
    return x * depth


assert task1('test.txt') == 150
assert task1('data.txt') == 1690020
assert task2('test.txt') == 900
assert task2('data.txt') == 1408487760
