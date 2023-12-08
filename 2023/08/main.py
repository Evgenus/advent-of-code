from collections import defaultdict, Counter
from functools import cache, partial
from itertools import repeat, cycle
from math import lcm

from utils import *
# load_input()


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    instructions = lines[0]

    network = {}
    for line in lines[2:]:
        src, dst = line.split(" = ")
        network[src] = dst[1:-1].split(", ")

    return instructions, network


def navigate(network, instructions, start):
    pos = start
    for step, move in enumerate(cycle(instructions)):
        if pos.endswith('Z'):
            return step
        pos = network[pos][move == 'R']


def task1(filename):
    instructions, network = read_data(filename)
    return navigate(network, instructions, 'AAA')


def task2(filename):
    instructions, network = read_data(filename)

    results = [
        navigate(network, instructions, pos)
        for pos in network
        if pos.endswith('A')
    ]

    return lcm(*results)


assert task1('test1.txt') == 6
assert task1('data.txt') == 20659
assert task2('test2.txt') == 6
assert task2('data.txt') == 15690466351717
