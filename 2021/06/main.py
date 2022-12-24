from collections import Counter

from utils import *


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return lmap(int, data.strip().split(','))


def task(filename, days):
    ages = read_data(filename)
    ages = Counter(ages)
    for day in range(days):
        next_ages = Counter()
        for age, count in ages.items():
            next_ages[age - 1] = count
        next_ages[6] += next_ages[-1]
        next_ages[8] += next_ages[-1]
        next_ages[-1] = 0
        ages = next_ages

    return ages.total()


assert task('test.txt', 80) == 5934
assert task('data.txt', 80) == 365862
assert task('test.txt', 256) == 26984457539
assert task('data.txt', 256) == 1653250886439
