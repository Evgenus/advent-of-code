from utils import *


def read_data(filename):
    with open(filename, 'r') as stream:
        data = stream.read()

    return data.strip().splitlines()


def task(filename, size):
    lines = read_data(filename)

    res = []
    for line in lines:
        for i, chunk in enumerate(iter_window(line, size)):
            if len(set(chunk)) == size:
                res.append(i + size)
                break
    return res


assert task('test.txt', 4) == [7, 5, 6, 10, 11]
assert task('test.txt', 14) == [19, 23, 23, 29, 26]
assert task('data.txt', 4) == [1582]
assert task('data.txt', 14) == [3588]
