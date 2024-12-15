from utils import *
from collections import Counter
from itertools import pairwise
from sympy import Symbol, Eq, solve
from sympy.core.numbers import Integer


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    lines = read_data(filename)
    result = 0

    parts = list_split(lines, [''])
    for a, b, p in parts:
        ax, ay = str_integers(a)
        bx, by = str_integers(b)
        px, py = str_integers(p)

        a = Symbol(f'a')
        b = Symbol(f'b')
        params = [a, b]
        equations = [
            Eq(px, ax * a + bx * b),
            Eq(py, ay * a + by * b),
        ]
        results = solve(equations, [a, b])
        if not isinstance(results[a], Integer):
            continue
        if not isinstance(results[b], Integer):
            continue
        result += results[a] * 3 + results[b]

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    parts = list_split(lines, [''])
    for a, b, p in parts:
        ax, ay = str_integers(a)
        bx, by = str_integers(b)
        px, py = str_integers(p)

        px += 10000000000000
        py += 10000000000000

        a = Symbol(f'a')
        b = Symbol(f'b')
        params = [a, b]
        equations = [
            Eq(px, ax * a + bx * b),
            Eq(py, ay * a + by * b),
        ]
        results = solve(equations, [a, b])
        if not isinstance(results[a], Integer):
            continue
        if not isinstance(results[b], Integer):
            continue
        result += results[a] * 3 + results[b]

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 480
assert task1('data.txt') == 30973
assert task2('data.txt') == 95688837203288
