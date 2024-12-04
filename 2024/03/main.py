from utils import *
from collections import Counter
from itertools import pairwise
load_input()

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()

def task1(filename):
    expr = re.compile("mul\((\d+),(\d+)\)")
    lines = read_data(filename)
    result = 0
    for line in lines:
        for a, b in re.findall(expr, line):
            result += int(a) * int(b)
    print(result)
    return result


def task2(filename):
    expr = re.compile("(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)")
    lines = read_data(filename)
    result = 0
    enabled = True
    for line in lines:
        for t, f, a, b in re.findall(expr, line):
            if f:
                enabled = False
            elif t:
                enabled = True
            elif enabled:
                result += int(a) * int(b)
    print(result)
    return result


assert task1('test1.txt') == 161
assert task1('data.txt') == 166357705
assert task2('test2.txt') == 48
assert task2('data.txt') == 88811886
