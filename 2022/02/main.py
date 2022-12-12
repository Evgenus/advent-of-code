def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    return data.strip().splitlines()


FIRST = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
}

SECOND1 = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S',
}

SCORE1 = {
    ('R', 'R'): 3 + 1,
    ('P', 'R'): 0 + 1,
    ('S', 'R'): 6 + 1,

    ('R', 'P'): 6 + 2,
    ('P', 'P'): 3 + 2,
    ('S', 'P'): 0 + 2,

    ('R', 'S'): 0 + 3,
    ('P', 'S'): 6 + 3,
    ('S', 'S'): 3 + 3,
}


def task1(filename):
    res = 0
    for line in read_data(filename):
        a, b = line.split()
        a, b = FIRST[a], SECOND1[b]
        res += SCORE1[a, b]
    return res


SECOND2 = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}


SCORE2 = {
    ('R', 'L'): 0 + 3,
    ('P', 'L'): 0 + 1,
    ('S', 'L'): 0 + 2,

    ('R', 'D'): 3 + 1,
    ('P', 'D'): 3 + 2,
    ('S', 'D'): 3 + 3,

    ('R', 'W'): 6 + 2,
    ('P', 'W'): 6 + 3,
    ('S', 'W'): 6 + 1,
}


def task2(filename):
    res = 0
    for line in read_data(filename):
        a, b = line.split()
        a, b = FIRST[a], SECOND2[b]
        res += SCORE2[a, b]
    return res


assert task1('test.txt') == 15
assert task2('test.txt') == 12
assert task1('data.txt') == 13484
assert task2('data.txt') == 13433
