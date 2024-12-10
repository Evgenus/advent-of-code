from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    result = 0
    line = deque(lines[0])
    num = 0
    files = []
    disk = deque()
    while line:
        file = int(line.popleft())
        for i in range(file):
            disk.append(num)
        if not line:
            break
        space = int(line.popleft())
        for i in range(space):
            disk.append('.')
        num += 1

    l = 0
    r = len(disk) - 1
    while l < r:
        while disk[l] != '.':
            l += 1
        while disk[r] == '.':
            r -= 1
        if l < r:
            disk[l], disk[r] = disk[r], disk[l]
        l += 1
        r -= 1

    result = sum(i * value for i, value in enumerate(disk) if value != '.')

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0
    line = deque(lines[0])
    num = 0
    p = 0
    files = []
    spaces = []
    disk = deque()
    while line:
        file = int(line.popleft())
        files.append((p, file, num))
        for i in range(file):
            disk.append(num)
            p += 1
        if not line:
            break
        space = int(line.popleft())
        spaces.append((p, space))
        for i in range(space):
            disk.append('.')
            p += 1
        num += 1

    while files:
        p, file, num = files.pop()
        for i in range(len(spaces)):
            t, space = spaces[i]
            if t > p:
                break
            if space >= file:
                spaces[i] = (t + file, space - file)
                for j in range(file):
                    disk[p + j] = '.'
                for j in range(file):
                    disk[t + j] = num
                break

    result = sum(i * value for i, value in enumerate(disk) if value != '.')

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 1928
assert task1('data.txt') == 6288599492129
assert task2('test.txt') == 2858
assert task2('data.txt') == 6321896265143
