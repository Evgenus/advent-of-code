from collections import Counter

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    (polymer,), srules = list_split(data.strip().splitlines(), [''])
    rules = {}
    for line in srules:
        a, b = line.split(' -> ')
        rules[a] = b
    return polymer, rules


def task(filename, steps):
    polymer, rules = read_data(filename)
    polymer += '.'
    counter = Counter()
    for a, b in iter_window(polymer, 2):
        counter[a + b] += 1
    for step in range(steps):
        new_counter = Counter()
        for (a, b), v in counter.items():
            if a + b in rules:
                c = rules[a + b]
                new_counter[a + c] += v
                new_counter[c + b] += v
            else:
                new_counter[a + b] += v
        counter = new_counter

    letters = Counter()
    for (a, b), v in counter.items():
        letters[a] += v
    return max(letters.values()) - min(letters.values())


assert task('test.txt', 10) == 1588
assert task('data.txt', 10) == 2027
assert task('test.txt', 40) == 2188189693529
assert task('data.txt', 40) == 2265039461737
