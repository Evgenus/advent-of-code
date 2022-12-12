from string import (
    ascii_lowercase,
    ascii_uppercase,
)

from utils import str_common


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


chars = {
    c: i
    for i, c in enumerate(ascii_lowercase + ascii_uppercase, 1)
}


def task1(filename):
    lines = read_data(filename)
    res = 0
    for line in lines:
        half = len(line) // 2
        common = str_common(line[:half], line[half:])[0]
        res += chars[common]
    return res


def task2(filename):
    lines = read_data(filename)
    res = 0
    for i in range(0, len(lines), 3):
        common = str_common(lines[i], lines[i + 1], lines[i + 2])[0]
        res += chars[common]
    return res


assert task1('test.txt') == 157
assert task2('test.txt') == 70
assert task1('data.txt') == 7793
assert task2('data.txt') == 2499
