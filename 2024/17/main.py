from utils import *
from collections import Counter
from itertools import pairwise

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


def run(A, B, C, program):
    out = []
    ptr = 0
    while ptr < len(program):
        op = program[ptr]
        val = program[ptr + 1]
        if val == 4:
            combo = A
        elif val == 5:
            combo = B
        elif val == 6:
            combo = C
        else:
            combo = val

        if op == 0: # adv
            A = A // (2 ** combo)
        elif op == 1:
            B = B ^ val
        elif op == 2:
            B = combo % 8
        elif op == 3:
            if A != 0:
                ptr = val
                continue
        elif op == 4:
            B = B ^ C
        elif op == 5:
            out.append(combo % 8)
        elif op == 6:
            B = A // (2 ** combo)
        elif op == 7:
            C = A // (2 ** combo)
        ptr += 2

    return ','.join(map(str, out))


def run2(A, B, C, program):
    out = []
    while A:
        B = A % 8
        B = B ^ 5
        C = A // (2 ** B)
        B = B ^ 6
        A = A // 8
        B = B ^ C
        out.append(B % 8)
    return ','.join(map(str, out))


def task1(filename):
    lines = read_data(filename)
    result = 0

    registers, program = list_split(lines, [''])
    A, B, C = [str_integers(reg)[0] for reg in registers]

    program = str_integers(program[0])

    result = run(A, B, C, program)

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    registers, program = list_split(lines, [''])
    A, B, C = [str_integers(reg)[0] for reg in registers]

    program = str_integers(program[0])
    expected = ','.join(map(str, program))
    g = expected[::-1].replace(',', '')
    p = 11

    A = 0o3002165110264632
    while True:
        output = run2(A, B, C, program)
        f = output[::-1].replace(',', '')
        if f[:p] == g[:p]:
            print(oct(A), f, g)
        # print(int(expected[::-1].replace(',', ''), 8))
        # print()
        if output == expected:
            result = A
            break
        A += 1
        # break

    print(f"2: {filename}, {result}")
    return result


load_input()
# assert task1('test.txt') == "4,6,3,5,6,3,5,2,1,0"
# assert task1('data.txt') == "1,2,3,1,3,2,5,3,1"
# assert task2('test.txt') == 0
assert task2('data.txt') == 0
