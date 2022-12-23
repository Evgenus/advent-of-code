from collections import Counter
from functools import partial

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(partial(lmap, int), data.strip().splitlines())


def task1(filename):
    bits = read_data(filename)
    most_common = [seq.count(1) > seq.count(0) for seq in zip(*bits)]
    gamma = int_from_bits(most_common)
    least_common = [seq.count(1) < seq.count(0) for seq in zip(*bits)]
    epsilon = int_from_bits(least_common)
    return gamma * epsilon


def get_bits(bits, pos):
    return [seq[pos] for seq in bits]


def task2(filename):
    bits = read_data(filename)

    pool = bits.copy()
    for i in range(len(bits[0])):
        at_pos = get_bits(pool, i)
        most_common = at_pos.count(1) >= at_pos.count(0)
        pool = [seq for seq in pool if seq[i] == most_common]
        if len(pool) == 1:
            break
    oxygen = int_from_bits(pool[0])

    pool = bits.copy()
    for i in range(len(bits[0])):
        at_pos = get_bits(pool, i)
        least_common = at_pos.count(1) < at_pos.count(0)
        pool = [seq for seq in pool if seq[i] == least_common]
        if len(pool) == 1:
            break
    co2 = int_from_bits(pool[0])

    return oxygen * co2


assert task1('test.txt') == 198
assert task1('data.txt') == 4147524
assert task2('test.txt') == 230
assert task2('data.txt') == 3570354
