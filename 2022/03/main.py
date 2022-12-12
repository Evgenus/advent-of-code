from string import (
    ascii_lowercase,
    ascii_uppercase,
)

from utils import str_common


def read_data():
    with open('data.txt', 'r') as f:
        data = f.read()

    lines = data.strip().splitlines()
    return lines


chars = {
    c: i
    for i, c in enumerate(ascii_lowercase + ascii_uppercase, 1)
}


def task1():
    lines = read_data()
    res = 0
    for line in lines:
        half = len(line) // 2
        common = str_common(line[:half], line[half:])[0]
        res += chars[common]
    return res


def task2():
    lines = read_data()
    res = 0
    for i in range(0, len(lines), 3):
        common = str_common(lines[i], lines[i + 1], lines[i + 2])[0]
        res += chars[common]
    return res


print(task1())
print(task2())
