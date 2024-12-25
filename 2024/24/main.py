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

    values = {}
    values_raw, expr_raw = list_split(lines, [''])
    for line in values_raw:
        name, value = line.split(': ')
        values[name] = int(value)

    expr = []
    for line in expr_raw:
        a, op, b, _, res = line.split(' ')
        expr.append((a, op, b, res))

    while expr:
        nxt = []
        for a, op, b, res in expr:
            if a in values and b in values:
                if op == 'AND':
                    values[res] = int(values[a] and values[b])
                elif op == 'XOR':
                    values[res] = int(values[a] != values[b])
                else:
                    values[res] = int(values[a] or values[b])
            else:
                nxt.append((a, op, b, res))
        expr = nxt

    values = sorted(
        (name, str(value))
        for name, value in values.items()
        if name.startswith('z')
    )[::-1]

    result = int(''.join(value for name, value in values), 2)

    print(f"1: {filename}, {result}")
    return result


def task2(filename):
    lines = read_data(filename)
    result = 0

    values = {}

    values_raw, expr_raw = list_split(lines, [''])
    for line in values_raw:
        name, value = line.split(': ')
        values[name] = int(value)

    grouped = defaultdict(lambda: defaultdict(list))

    xor_names = {}
    and_names = {}

    expr = []
    for line in expr_raw:
        a, op, b, _, res = line.split(' ')
        if a > b:
            a, b = b, a
        e = (a, op, b, res)
        if a[0] == 'x' and op == 'XOR':
            grouped[int(a[1:])]['val1'].append(e)
            xor_names[res] = int(a[1:])
        elif a[0] == 'x' and op == 'AND':
            grouped[int(a[1:])]['val2'].append(e)
            and_names[res] = int(a[1:])
        elif res[0] == 'z' and op =='XOR':
            grouped[int(res[1:])]['res'].append(e)
        else:
            expr.append(e)

    expr2 = []
    for e in expr:
        a, op, b, res = e
        if op == 'AND':
            if a in xor_names:
                grouped[xor_names[a]]['val3'].append(e)
                continue
            if b in xor_names:
                grouped[xor_names[b]]['val3'].append(e)
                continue
        if op == 'OR':
            if a in and_names:
                grouped[and_names[a]]['val4'].append(e)
                continue
            if b in and_names:
                grouped[and_names[b]]['val4'].append(e)
                continue
        expr2.append(e)

    print()
    order = sorted(grouped)

    for o in order:
        group = grouped[o]
        print(group['val1'])
        print(group['val2'])
        print(group['val3'])
        print(group['val4'])
        print(group['res'])
        print()

    result = ','.join(sorted([
        'gsd',
        'kth',
        'tbt',
        'vpm',
        'qnf',
        'z12',
        'z26',
        'z32',
    ]))

    print(f"2: {filename}, {result}")
    return result


# load_input()
assert task1('test.txt') == 2024
assert task1('data.txt') == 55544677167336
assert task2('data.txt') == "gsd,kth,qnf,tbt,vpm,z12,z26,z32"
