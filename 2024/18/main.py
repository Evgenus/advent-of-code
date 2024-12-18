from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename, n, cap):
    lines = read_data(filename)
    result = 0
    memory = [
        ['.'] * n
        for _ in range(n)
    ]
    for line in lines[:cap]:
        j, i = str_integers(line)
        memory[i][j] = '#'

    queue = [(0, 0)]
    used = defaultdict(lambda: 10 ** 6)
    step = 1
    while queue:
        nxt = []
        for i, j in queue:
            for ni, nj in matrix_next4(memory, i, j):
                if memory[ni][nj] == '#':
                    continue
                if used[ni, nj] <= step:
                    continue
                used[ni, nj] = step
                nxt.append((ni, nj))
        queue = nxt
        step += 1

    # matrix_print(memory)

    result = used[n - 1, n - 1]

    print(f"1: {filename}, {result}")
    return result


def task2(filename, n, cap):
    lines = read_data(filename)
    for c in range(cap, len(lines) + 1):
        memory = [
            ['.'] * n
            for _ in range(n)
        ]
        for line in lines[:c]:
            j, i = str_integers(line)
            memory[i][j] = '#'

        queue = [(0, 0)]
        used = defaultdict(lambda: 10 ** 6)
        step = 1
        while queue:
            nxt = []
            for i, j in queue:
                for ni, nj in matrix_next4(memory, i, j):
                    if memory[ni][nj] == '#':
                        continue
                    if used[ni, nj] <= step:
                        continue
                    used[ni, nj] = step
                    nxt.append((ni, nj))
            queue = nxt
            step += 1

        if  used[n - 1, n - 1] > n * n:
            result = line
            break

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt', 7, 12) == 22
assert task1('data.txt', 71, 1024) == 226
assert task2('test.txt', 7, 12) == '6,1'
assert task2('data.txt', 71, 1024) == '60,46'
